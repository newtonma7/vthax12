import time
from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

#open css file
#with open('pages/style.css') as file:
#    css = file.read()
#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Set your OpenAI API key
load_dotenv()
apiKey=str(os.getenv("KEY"))
client = OpenAI(api_key=apiKey)

def generate(text):
    response = client.images.generate(
        model="dall-e-3",
        prompt=text,
        n=1,
        size="1024x1024",
        quality="hd",
    )
    #return image URL
    return response.data[0].url

#clicked button function
def click_button():
    st.session_state.clicked = True


#title
st.title("Goku Guesses 😎")
st.markdown("Lets see what your home could look like.")
key = st.text_input("Please proivde your OpenAI key (Leave blank if .env is set up)")
if key != "":
    client = OpenAI(api_key=key)
st.divider()

#organization
col1, col2 = st.columns(2)
with col1:
    age = st.slider("What's your age?", 18, 100, 25)
    relationship = st.checkbox("Consider partner salary?")
    if (relationship):
        partnerSal = st.number_input("Partner's salary?", value=50000)
with col2:
    loc = st.text_input("Where do you want to live?")
    salary = st.number_input("Salary?", value=50000)
submit = st.button("Show my potential home :D", on_click=click_button)
col3, col4 = st.columns(2)

#init picture history list
if "picture" not in st.session_state:
    st.session_state.picture = []

#print previous picture
with col3:
    placeholder = st.empty()
for picture in st.session_state.picture:
    with col3:
        old = placeholder.image(picture)

if submit:
    #prompt
    if (loc != ''):
        old = None
        if (relationship):
            prompt = "Generate a realistic image of a house that I can afford given a yearly salary of " + str(salary + partnerSal) + " and a desired monthly mortgage payment of " + str((salary + partnerSal)/12 * 0.26) + " in " + loc
        else:
            prompt = "Generate a realistic image of a house that I can afford given a yearly salary of " + str(salary) + " and a desired mortgage payment of " + str((salary)/12 * 0.26) + " in " + loc
        # get image
        image_url = generate(prompt)
        # Display the image
        with col3:
            st.image(image_url, caption="Generated Image")
        #add image to array and empty the current
        st.session_state.picture = []
        st.session_state.picture.append(image_url)
        placeholder.empty()
        time.sleep(3)
    else:
        st.warning("Please enter all fields to generate an image.")

#chat on the side
prompt = st.chat_input("Start chatting")
with col4:
    #initial message from Goku
    Goku = st.chat_message("assistant", avatar='🧸')
    Goku.write("👋 Hello! Ask about your potential house here!🏠")

    #init chat history list
    if "messages" not in st.session_state:
        st.session_state.messages2 = []

    #chat box
    for message in st.session_state.messages2:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user = st.chat_message("user")
    if prompt:
        pic = None
        for url in st.session_state.picture:
            pic = url 
        user.markdown(prompt)
        st.session_state.messages2.append({"role": "user", "content": prompt})
        #Goku response
        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": [
                        {"type": "text","text": prompt},
                    {"type": "image_url", "image_url": {
                        "url": pic,
                        },
                    },
                    ],
                }
                ],
                stream = True,
                max_tokens= 500 #changeable
            )
            response = st.write_stream(stream)        
        st.session_state.messages2.append({"role": "assistant", "content": response})

