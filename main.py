import streamlit as st
from streamlit_chat import message
from utils import process_query
import streamlit as st

# Initializing the initial message st.session_states
if "res" not in st.session_state:
    st.session_state.res = ["How can I assist you?"]

if "req" not in st.session_state:
    st.session_state.req = []

if "disabled" not in st.session_state:
    st.session_state.disabled = False

# Interface

st.header("🦜Parrots GPT")

# Container for Chat History
response_container = st.container()

# Container for text box
textcontainer = st.container()

# Display for the loading the request by the user
with textcontainer:
    query = st.text_input("Query: ", key="input",
                          disabled=st.session_state.disabled)
    is_clicked = st.button("Send Input")
    if is_clicked:
        with st.spinner("typing..."):
            response = process_query(query)
            st.session_state.req.append(query)
            st.session_state.res.append(response)
            is_clicked = False

# Display of the chat history
with response_container:
    if st.session_state.res:
        for i in range(len(st.session_state.res)):
            message(st.session_state.res[i], key=str(i), logo = f'https://post.healthline.com/wp-content/uploads/2020/08/lychees-732x549-thumbnail-732x549.jpg')
            if i < len(st.session_state.req):
                message(st.session_state.req[i],
                        is_user=True, key=str(i) + "_user", logo = f'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Oranges_-_whole-halved-segment.jpg/640px-Oranges_-_whole-halved-segment.jpg')
