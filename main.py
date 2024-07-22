import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
api_host = os.environ.get("PATHWAY_REST_CONNECTOR_HOST", "127.0.0.1")
api_port = int(os.environ.get("PATHWAY_REST_CONNECTOR_PORT", "8080"))

with st.sidebar:
    st.markdown("View the chat history of the queries so far here")
    if st.button("Clear Chat History"):
        st.session_state.messages = []

st.title("DevMate")
st.header("Introduction")
st.markdown(
    """
    Welcome to DevMate! Your personal coding assistant that helps you with code-related queries, troubleshooting, and more. 
    Ask any programming questions, and receive answers and instant code snippets tailored to your needs.
    """
)

st.header("How to Use DevMate?")
st.markdown(
    """
    1. Type your query in the chat input box below.
    2. Receive instant responses and guidance.
    3. View the chat history for reference.
    """
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Hello, How can I help you today?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    url = f"http://{api_host}:{api_port}/"
    data = {"query": prompt, "user": "user"}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        response_json = response.json()
        with st.chat_message("assistant"):
            st.markdown(response_json)
        st.session_state.messages.append({"role": "assistant", "content": response_json})
    else:
        st.error(f"Error {response.status_code} :Failed to send data.")
