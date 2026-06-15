import streamlit as st
import base64

def set_background():

    with open("assets/background.jpg", "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.set_page_config(
    page_title="Login",
    page_icon="🧭",
    layout="wide"
)
set_background()

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
    
    
    
