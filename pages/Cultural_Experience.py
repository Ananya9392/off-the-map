import streamlit as st

if st.button("⬅ Back"):
    st.switch_page("pages/home.py")

st.title("🎭 Cultural Experience")

st.image("assets/culture.jpg")

st.subheader("About")
st.write("""
Experience Assam's traditional dance,
music and vibrant local festivals.
""")

st.subheader("Posted By")
st.write("Ananya")


