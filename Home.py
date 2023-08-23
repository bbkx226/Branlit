import streamlit as st
from htmlTemplates import button_css

# Set page config
st.set_page_config(page_title="Branlit", page_icon=":brain:", layout="centered") 

st.write("")

# Add CSS style
st.markdown(button_css, unsafe_allow_html=True)

# Page title 
st.title("Welcome to Branlit! :wave:")

# Info text
st.write("This is the homepage for my cool new app. Here are some things you can do:")

st.sidebar.success("☝️☝️☝️ Features above ☝️☝️☝️")

# Button 1
if st.button("Button 1"):
    st.write("You clicked Button 1")

# Button 2 
if st.button("Button 2"):
    st.write("You clicked Button 2")

# Button 3
if st.button("Button 3"):
    st.write("You clicked Button 3")