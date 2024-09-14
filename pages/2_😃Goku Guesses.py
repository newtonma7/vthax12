from openai import OpenAI
import streamlit as st
from PIL import Image
from io import BytesIO

#open css file
#with open('pages/style.css') as file:
#    css = file.read()
#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Set your OpenAI API key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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


#title
st.title("Goku Guesses 😎")
st.markdown("Lets see what your home could look like.")
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

if st.button("Show my potential home :D"):
    #prompt
    if (loc != ''):
        if (relationship):
            prompt = "Generate a realistic image of a house that I can afford based on the following details: age" + str(age)
            prompt+= " Location: " + loc + " Salary a year in USD: " + str(salary + partnerSal) + "keep in mind the costs of houses in these locations"
        else:
            prompt = "Generate a realistic image of a house that I can afford based on the following details: age" + str(age)
            prompt+= " Location: " + loc + " Salary a year in USD: " + str(salary) + "keep in mind the costs of houses in these locations"
        # get image
        image_url = generate(prompt)
        # Display the image
        st.image(image_url, caption="Generated Image")
    else:
        st.warning("Please enter all fields to generate an image.")
