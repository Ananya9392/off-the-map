import streamlit as st

st.title("Login")

name = st.text_input("Name")
phone = st.text_input("Mobile Number")

st.button("Login / Sign Up")
