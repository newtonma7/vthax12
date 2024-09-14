import streamlit as st
import time

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


st.title("hello, this is goku")
st.divider()
st.markdown("Hello! Chat with me.")
#initial message from Goku
Goku = st.chat_message("Goku")
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
    with st.chat_message("Goku"):
        response = st.write_stream(test())
    st.session_state.messages.append({"role": "Goku", "content": response})
