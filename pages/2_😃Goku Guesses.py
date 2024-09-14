from openai import OpenAI
import streamlit as st
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
from PIL import Image
from io import BytesIO

#import streamlit as st
#import time
#from openai import OpenAI

#title
st.title("Goku Guesses 😎")
st.markdown("Lets see what your home could look like.")

if "GPT" not in st.session_state:
    st.session_state["GPT"] = "gpt-3.5-turbo"
#openai.api_key =

# Set your OpenAI API key


# Input prompt from the user
prompt = st.text_input("Enter a prompt for the image:")

if st.button("Show my potential home :D"):
    if prompt:
        # Generate image using OpenAI
        response = client.images.generate(prompt=prompt,
        n=1,
        model= st.session_state["GPT"],
        size="512x512"
        )

        # Get the image URL
        image_url = response.data[0].url

        # Display the image
        st.image(image_url, caption="Generated Image")
    else:
        st.warning("Please enter a prompt to generate an image.")
