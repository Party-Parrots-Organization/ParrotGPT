import pinecone
from sentence_transformers import SentenceTransformer
import openai
import streamlit as st
from os import environ
from dotenv import load_dotenv
from langchain.chains import ConversationChain, SequentialChain
from langchain.chains.question_answering import load_qa_chain
from langchain.chains.openai_functions.openapi import get_openapi_chain
import urllib.parse
# chain = get_openapi_chain("https://www.klarna.com/us/shopping/public/openai/v0/api-docs/")

load_dotenv()
model = SentenceTransformer("all-MiniLM-L6-v2")

url = "https://api-ap.hosted.exlibrisgroup.com/primo/v1/search?" + urllib.parse.urlencode({
    "vid": "65SMU_INST%3ASMU_NUI",
    "lang": "eng",
    "offset": 0,
    "limit": 10,
    "sort": "rank",
    "pcAvailability": "true",
    "getMore": 0,
    "conVoc": "true",
    "inst": "65SMU_INST",
    "skipDelivery": "true",
    "disableSplitFacets": "true",
    "apikey": environ.get("PRIMO_API_KEY")
})

openai.api_key = environ.get("OPENAI_API_KEY")
pinecone.init(api_key=environ.get("PINECONE_API_KEY"),
              environment=environ.get("PINECONE_ENVIRONMENT"))
index = pinecone.Index(environ.get("PINECONE_INDEX"))


def process_query(query: str, conversation_chain: ConversationChain):
    refined_query = query_refiner(get_conversation_string(), query)
    pinecone_context = find_pinecone_match(refined_query)
    # response returns a string which contains a list of resources which match the query string
    response = conversation_chain.predict(
        input=f"Context:\n {pinecone_context} \n\n Query: \n {query}")
    api_chain =    # print(api_chain(response))
    print("==========================")
    print(pinecone_context[0])
    print("==========================")
    return 


def query_refiner(conversation, query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base.\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\nRefined Query:",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']


def find_pinecone_match(input):

    input_em = model.encode(input).tolist()
    result = index.query(input_em,
                         top_k=2, includeMetadata=True)
    if (len(result.matches) == 0):
        return "No context"
    return result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']


def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state.res) - 1):
        conversation_string += "Human: "+st.session_state.req[i] + "\n"
        conversation_string += "Bot: " + \
            st.session_state.res[i+1] + "\n"
    return conversation_string
