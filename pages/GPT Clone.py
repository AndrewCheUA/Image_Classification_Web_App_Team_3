import streamlit as st
import openai as openai

from function.sidebar import sidebar

st.set_page_config(page_title="Web_App_Team_3", page_icon="🤖", layout="wide")

st.title("ChatGPT-clone")

openai.api_key = st.secrets["OPEN_API_KEY"]

api_key = sidebar()

if not api_key:
    st.error(
        "⚠️ You haven't provided an API key. Please enter your API key in the sidebar.\n"
        "You can get an API key from [OpenAI](https://platform.openai.com/account/api-keys)."
    )
else:
    openai.api_key = api_key

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messaes" not in st.session_state:
    st.session_state.messages = []
# display chat messages from history on add return
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
prompt = st.chat_input("What is up?")
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(model=st.session_state["openai_model"],
                                                     messages=[
                                                         {"role": m["role"], "content": m["content"]}
                                                         for m in st.session_state.messages
                                                     ], stream=True
                                                     ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "! ")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
