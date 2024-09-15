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

# image files
logo = "gallery/logo.png"
full_logo = "gallery/fulllogo.png"

# function that uses CSS to design a style for the sidebar logo to make it bigger and generate it
def set_logo_size():
    st.markdown("""<style>
    div[data-testid="stSidebarHeader"] > img, div[data-testid="collapsedControl"] > img {
        height: 7rem;
        width: auto;
    }
    
    div[data-testid="stSidebarHeader"], div[data-testid="stSidebarHeader"] > *,
    div[data-testid="collapsedControl"], div[data-testid="collapsedControl"] > * {
        display: flex;
        align-items: center;
    }
    </style>""", unsafe_allow_html=True)

    # displays the logo in the sidebar - collapsable
    st.logo(
        full_logo,
        icon_image=logo,
    )

set_logo_size()

#intro
st.title("Hello! I'm Goku")
st.divider()

#set up openai 
if "GPT" not in st.session_state:
    st.session_state["GPT"] = "gpt-4-turbo"

#initial message from Goku
key = st.text_input("Please proivde your OpenAI key (Leave blank if .env is set up)")
if key != "":
    client = OpenAI(api_key=key)
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
