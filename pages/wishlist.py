import streamlit as st

st.set_page_config(page_title="Wishlist")

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

if st.button("⬅"):
    st.switch_page("pages/home.py")

st.title("🔖 Wishlist")

for place in st.session_state.wishlist:
    st.write("📍", place)




