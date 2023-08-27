import pinecone
from sentence_transformers import SentenceTransformer
import openai
import streamlit as st
from os import environ
from dotenv import load_dotenv
from llm import conversation_chain

load_dotenv()
model = SentenceTransformer("all-MiniLM-L6-v2")

openai.api_key = environ.get("OPENAI_API_KEY")
pinecone.init(api_key=environ.get("PINECONE_API_KEY"),
              environment=environ.get("PINECONE_ENVIRONMENT"))
index = pinecone.Index(environ.get("PINECONE_INDEX"))


def process_query(query: str):
    refined_query = query_refiner(get_conversation_string(), query)
    pinecone_context = find_pinecone_match(refined_query)
    response = conversation_chain.predict(
        input=f"Context:\n {pinecone_context} \n\n Query: \n {query}")
    return response


def query_refiner(conversation, query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base. If not possible, just return the user request instead\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\nRefined Query:",
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

    matches = []
    print(result.matches)
    for match in result.matches:
        if match.score >= 0.65:
            matches.append(match)
    if len(matches) == 0:
        return "No context"
    else:
        return list(map(lambda x: x["metadata"]["text"], matches))


def get_conversation_string():

    conversation_string = ""
    for i in range(len(st.session_state.res) - 1):

        if len(st.session_state.req) < 4 or i > len(st.session_state.req) - 4:
            conversation_string += "Human: "+st.session_state.req[i] + "\n"
            conversation_string += "Bot: " + \
            st.session_state.res[i+1] + "\n"
        else:
            pass

    print(conversation_string)
    return conversation_string
