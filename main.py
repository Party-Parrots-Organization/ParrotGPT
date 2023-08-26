import streamlit as st
from streamlit_chat import message
from utils import process_query
from langchain.chains import ConversationChain
from llm import llm, prompt_template
import streamlit as st
from langchain.chains.conversation.memory import ConversationBufferWindowMemory


# Initializing the initial message st.session_states
if "res" not in st.session_state:
    st.session_state.res = ["How can I assist you?"]

if "req" not in st.session_state:
    st.session_state.req = []
if 'buffer_memory' not in st.session_state:
    st.session_state.buffer_memory = ConversationBufferWindowMemory(
        k=3, return_messages=True)

conversation = ConversationChain(
    memory=st.session_state.buffer_memory, prompt=prompt_template, llm=llm, verbose=True)


# Interface

st.header("SMU Library Chatbot")

# Container for Chat History
response_container = st.container()

# Container for text box
textcontainer = st.container()

# Display for the loading the request by the user
with textcontainer:
    query = st.text_input("Query: ", key="input")
    if query:
        with st.spinner("typing..."):
            response = process_query(query, conversation)
            st.session_state.req.append(query)
            st.session_state.res.append(response)

# Display of the chat history
with response_container:
    if st.session_state.res:
        for i in range(len(st.session_state.res)):
            message(st.session_state.res[i], key=str(i))
            if i < len(st.session_state.req):
                message(st.session_state.req[i],
                        is_user=True, key=str(i) + "_user")
