import streamlit as st
col1, col2 = st.columns([1,8])

with col1:
    if st.button("⬅"):
        st.switch_page("pages/home.py")

with col2:
    st.title("➕ Add Place")


place = st.text_input("Place Name")

category = st.selectbox(
    "Category",
    ["Beach","Food","Culture","Shopping","Nature"]
)

location = st.text_input("Location")

description = st.text_area(
    "What makes it special?"
)

rating = st.slider(
    "Rating",
    1,
    5
)

image = st.file_uploader(
    "Upload Image"
)

if st.button("Post"):
    st.success("Post Uploaded")

    st.markdown("""
<style>

[data-testid="stSidebar"]{
    display:none;
}

</style>
""", unsafe_allow_html=True)


