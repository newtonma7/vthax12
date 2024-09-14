import streamlit as st

# sets the page layout to wide to fill up the page
st.set_page_config(layout='wide')

# adds a Home heading to the sidebar
st.sidebar.markdown("Home")

# image files
logo = "gallery/logo.png"
full_logo = "gallery/fulllogo.png"
house = "gallery/house.jpg"

# defines a style using CSS for the sidebar logo to make it bigger
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

# uses columns to display title and image on same line
col1, mid, col2 = st.columns([20,1,10.5])

# column 1 is title text
with col1:
    st.title("Welcome to _:orange[Goku Homes]_!")

# column 2 is logo
with col2:
    st.write("\n")
    st.image(logo, width=65)

# displays images of houses
st.image(house, width = 880)

# uses columns to display about us and contact info
col1, col2 = st.columns(2)

# column 1 is about us tab
with col1:
    st.header("About Us", divider="grey")
    about_us = '''Founded by Virginia Tech students, Goku Homes is a house finder application. Using OpenAI, Goku makes finding the perfect home for you in as easy as a few questions.'''
    st.markdown(about_us, unsafe_allow_html=True)

# column 2 is contact info tab
with col2:
    st.header("Contact Us", divider="grey")
    contact_info = '''Goku Homes  
    571-334-6471  
    gokuhomes@gmail.com
    '''
    st.markdown(contact_info, unsafe_allow_html=True)