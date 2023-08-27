import pinecone
from sentence_transformers import SentenceTransformer
import openai
import streamlit as st
from os import environ
from dotenv import load_dotenv

load_dotenv()

openai.api_key = environ.get("OPENAI_API_KEY")
pinecone.init(api_key=environ.get("PINECONE_API_KEY"),
              environment=environ.get("PINECONE_ENVIRONMENT"))
index = pinecone.Index(environ.get("PINECONE_INDEX"))


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


def find_match(input):
    input_em = SentenceTransformer("all-MiniLM-L6-v2").encode(input).tolist()
    result = index.query(input_em,
                         top_k=2, includeMetadata=True)
    if (len(result.matches) == 0):
        return "No context"
    return result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']


def get_conversation_string():

    conversation_string = ""
    for i in range(len(st.session_state.res) - 1):

        if len(st.session_state.req) < 4 or i > len(st.session_state.req) - 4:
            print("its a sucess!")
            conversation_string += "Human: "+st.session_state.req[i] + "\n"
            conversation_string += "Bot: " + \
            st.session_state.res[i+1] + "\n"
        else:
            print("remove this")

    print(conversation_string)
    return conversation_string
