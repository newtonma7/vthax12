import streamlit as st
import time
from openai import OpenAI
from PIL import Image
import os
from dotenv import load_dotenv

load_dotenv()
apiKey=str(os.getenv("KEY"))
client = OpenAI(api_key=apiKey)

#new assistant page
st.set_page_config(
    page_title = "Talk to Goku!",
    page_icon= "🧸",
)

#intro
st.title("Hello! I'm Goku")
st.divider()

#set up openai 
if "GPT" not in st.session_state:
    st.session_state["GPT"] = "gpt-4-turbo"

#initial message from Goku
Goku = st.chat_message("assistant", avatar='🧸')
Goku.write("👋 How may I help you on your house search today?🏠")

#init chat history list
if "messages" not in st.session_state:
    st.session_state.messages = []

#chat box
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Start chatting")
user = st.chat_message("user")
if prompt:
    user.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    #Goku response
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model= st.session_state["GPT"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream = True,
            max_tokens= 500 #changeable
        )
        response = st.write_stream(stream)        
    st.session_state.messages.append({"role": "assistant", "content": response})
