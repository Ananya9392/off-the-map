import streamlit as st
import base64

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Off The Map",
    page_icon="🧭",
    layout="wide"
)

# =========================
# BACKGROUND
# =========================

with open("assets/mountains.jpg", "rb") as image:
    encoded_bg = base64.b64encode(image.read()).decode()

st.markdown(
    f"""
    <style>

    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_bg}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stSidebar"] {{
        display:none;
    }}

    .login-card {{
        background: rgba(0,0,0,0.55);
        backdrop-filter: blur(12px);
        padding: 35px;
        border-radius: 25px;
        max-width: 500px;
        margin: auto;
        margin-top: 20px;
    }}

    h1,h2,h3,h4,h5,h6,p,label {{
        color:white !important;
    }}

    .stTextInput input {{
        border-radius:15px;
    }}

    .stButton button {{
        width:100%;
        border-radius:15px;
        height:50px;
        font-size:18px;
        font-weight:bold;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# LOGO
# =========================

st.markdown("<br>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([2,2,2])

with col2:
    st.image("assets/logo.png", width=220)

# =========================
# TITLE
# =========================

st.markdown(
    """
    <h1 style='text-align:center;'>
    OFF THE MAP
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <h4 style='text-align:center;'>
    Discover Hidden Gems Around The World
    </h4>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# =========================
# LOGIN CARD
# =========================

st.markdown('<div class="login-card">', unsafe_allow_html=True)

name = st.text_input(
    "👤 Name",
    placeholder="Enter your name"
)

email = st.text_input(
    "📧 Email",
    placeholder="Enter your email"
)

phone = st.text_input(
    "📱 Phone Number",
    placeholder="Enter your phone number"
)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 Login / Sign Up"):

    st.session_state["name"] = name
    st.session_state["email"] = email
    st.session_state["phone"] = phone

    st.switch_page("pages/home.py")

st.markdown("</div>", unsafe_allow_html=True)
