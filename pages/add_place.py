import streamlit as st

st.title("Add Place")

st.text_input("Place Name")

st.selectbox(
    "Category",
    ["Beach","Food","Culture","Shopping","Nature"]
)

st.text_input("Location")

st.text_area("What makes it special?")

st.file_uploader("Upload Photo")

st.button("Save")
