import streamlit as st
import Clipper
    
st.header("Copy to clipboard Demo")

# get a string from user 
input_txt = st.text_input("Enter a string to be copied")

# call the clip method to copy the string to system clipboard
Clipper.clip(input_txt) 

# option for user to check whether the code is working
if input_txt:
    st.text_input("Press Ctrl + V") # In browser, user can do 'ctrl + V' to check 

    

   
    