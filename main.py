import streamlit as st
from streamlit_chat import message
from utils import find_match, get_conversation_string, query_refiner
from langchain.chains import ConversationChain
from llm import llm, prompt_template
import streamlit as st
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
# from langchain.chains.openai_functions.openapi import get_openapi_chain
# chain = get_openapi_chain("https://www.klarna.com/us/shopping/public/openai/v0/api-docs/")
# chain("What are some options for a men's large blue button down shirt")

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
            # The get_conversation might need to revert back to getconversation_string() instead
            refined_query = query_refiner(get_conversation_string(), query)
            
            # Printing of refined query (Development Purpose)
            st.subheader("Refined Query:")
            st.write(refined_query)

            # From vector database
            context = find_match(refined_query)

            # st.session_state.buffer_memory
            response = conversation.predict(
                input=f"Context:\n {context} \n\n Query: \n {query}")
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
