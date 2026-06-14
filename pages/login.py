import streamlit as st

st.set_page_config(
    page_title="Login",
    page_icon="🧭",
    layout="wide"
)

# LOGIN TITLE

st.markdown("""
<h1 style='text-align:center;
color:#00D4FF;
font-size:60px;'>
🧭 OFF THE MAP
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;color:white;'>
Login to start discovering hidden gems
</h3>
""", unsafe_allow_html=True)

st.markdown("---")

# USER DETAILS

name = st.text_input("👤 Name")

email = st.text_input("📧 Email")

phone = st.text_input("📱 Phone Number")

# LOGIN BUTTON

if st.button("Login / Sign Up"):

    st.session_state["name"] = name
    st.session_state["email"] = email
    st.session_state["phone"] = phone

    st.switch_page("pages/home.py")
    
