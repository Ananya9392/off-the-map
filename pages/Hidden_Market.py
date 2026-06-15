import streamlit as st

if st.button("⬅ Back"):
    st.switch_page("pages/home.py")

st.title("🛍 Hidden Market")

st.image("assets/market.jpg")

st.subheader("About")
st.write("""
A local market known for handmade products,
traditional jewellery and authentic souvenirs.
""")

st.subheader("Posted By")
st.write("Ananya")


