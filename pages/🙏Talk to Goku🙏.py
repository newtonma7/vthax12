import streamlit as st
import time
from openai import OpenAI

def test():
    response = "Hello Hello hello hello"
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

#new assistant page
st.set_page_config(
    page_title = "🙏 Talk to Goku! 🙏",
    page_icon= "💀",
)

#intro
st.title("hello, this is goku")
st.divider()
st.markdown("Hello! Chat with me.")

#set up openai 
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
if "GPT" not in st.session_state:
    st.session_state["GPT"] = "gpt-3.5-turbo"

#initial message from Goku
Goku = st.chat_message("assistant")
Goku.write("👋 Hello! \nHow may I help you today")

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
            max_tokens= 30 #changeable
        )
        response = st.write_stream(stream)        
    st.session_state.messages.append({"role": "assistant", "content": response})
