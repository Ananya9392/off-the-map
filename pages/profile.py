import streamlit as st

col1, col2 = st.columns([1,8])

with col1:
    if st.button("⬅"):
        st.switch_page("pages/home.py")

with col2:   # Change title for each page
 st.title("👤 My Profile")

st.write("Name: Ananya")
st.write("Email: ananya@email.com")
st.write("Phone: +91 XXXXX XXXXX")
st.markdown("""
<style>

[data-testid="stSidebar"]{
    display:none;
}

</style>
""", unsafe_allow_html=True)

st.markdown("---")

st.button("Edit Profile")
st.button("Settings")



