###
# Class that represents the home page
#
# Authors: Richard Nguyen, Newton Ma, Timothy Tran
# Date: 09/14/2024
# VTHACKS12
###

import streamlit as st

# sets the page layout to wide to fill up the page
st.set_page_config(
    page_title = "🏠Home",
    layout='wide')

# image files
logo = "gallery/logo.png"
full_logo = "gallery/fulllogo.png"
house0 = "gallery/houses/house0.jpeg"
house1 = "gallery/houses/house1.jpeg"
house2 = "gallery/houses/house2.jpeg"
house3 = "gallery/houses/house3.jpeg"
house4 = "gallery/houses/house4.jpeg"
house5 = "gallery/houses/house5.jpeg"

### Functions that use CSS and markdown to set fonts, sizes, or images
# function that uses CSS to set the app's background to an unpacked image from url
def set_app_bg_hack_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://i.pinimg.com/736x/07/5e/34/075e3467e810d8abf135553f53ae4b2f.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# function that uses CSS to set the app's header to an unpacked image from url
def set_header_bg_hack_url():
    st.markdown(
         f"""
         <style>
         [data-testid="stHeader"] {{
             background: url("https://i.pinimg.com/736x/07/5e/34/075e3467e810d8abf135553f53ae4b2f.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )     

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

# calls functions to change the app and header backgrounds
set_app_bg_hack_url()
set_header_bg_hack_url()
set_logo_size()

### Uses columns to display images and text on the website aesthetically
# uses columns to display title and image on same line
welcome_col, mid, logo_col = st.columns([20,1,1.5])

# column 1 is title text
with welcome_col:
    st.title("Welcome to _:orange[Goku Homes]_!")

# column 2 is blank space

# column 3 is logo
with logo_col:
    st.write("\n")
    st.image(logo, width=80)

# uses columns to display title and image on same line
col1, col2, col3 = st.columns(3)

# column 1 is title text
with col1:
    st.image(house0, width=400)
    st.image(house1, width=400)

# column 2 is blank space
with col2:
    st.image(house2, width=400)
    st.image(house3, width=400)

# column 3 is logo
with col3:
    st.image(house4, width=400)
    st.image(house5, width=400)

# uses columns to display about us and contact info
about_us_col, our_vision_col, contact_col = st.columns([2,2,2], gap='medium')

# column 1 is about us tab
with about_us_col:
    st.header("About Us", divider="gray")
    about_us = '''Welcome to Goku Homes – Your Smart Home Finder!


Goku Homes is an innovative house-finding platform created by 
a passionate team of Virginia Tech students. Our mission is 
to simplify the home buying or renting process by integrating 
cutting-edge technology into real estate. With Goku Homes, finding 
the perfect home for you and your family has never been easier.


At the heart of our platform is Goku, your personal AI-powered realtor, 
powered by OpenAI. Goku is designed to guide you every step of the way 
by asking simple questions and understanding your preferences. Whether 
you’re searching for a cozy apartment, a sprawling farmhouse, or a modern 
condo, Goku helps you explore a variety of options based on your unique needs, 
budget, and location.'''

    st.markdown(about_us, unsafe_allow_html=True)

# column 2 is our vision tab
with our_vision_col:
    st.header("Our Vision", divider="gray")
    our_vision = '''We believe that finding a home should be stress-free, enjoyable, and most importantly, tailored to your needs. At Goku Homes, we’re blending real estate with AI technology to bring you a seamless, smart, and personalized home-finding experience.

Whether you’re buying your first home, relocating to a new city, or finding the perfect rental, Goku Homes is dedicated to helping you make the best decision with confidence.'''

    st.markdown(our_vision, unsafe_allow_html=True)

# column 3 is contact info tab
with contact_col:
    st.header("Contact Us", divider="gray")
    contact_info = '''Goku Homes  
    📞 571-334-6471  
    📧 gokuhomes@gmail.com
    '''
    st.markdown(contact_info, unsafe_allow_html=True)