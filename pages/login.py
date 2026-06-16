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

with open("assets/background.jpg", "rb") as image:
    encoded_bg = base64.b64encode(image.read()).decode()

st.markdown(
    f"""
    <style>

    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded_bg}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stSidebar"] {{
        display: none;
    }}

    h1, h2, h3, h4, h5, h6, p, label {{
        color: white !important;
    }}

    .stTextInput input {{
        border-radius: 15px;
    }}

    .stButton button {{
        width: 100%;
        height: 50px;
        border-radius: 15px;
        font-size: 18px;
        font-weight: bold;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# SPACING
# =========================

st.markdown("<br><br>", unsafe_allow_html=True)

# =========================
# CENTER LOGO
# =========================

left, center, right = st.columns([2,1,2])

with center:
    st.image(
        "assets/logo.jpg",
        width=220
    )

# =========================
# TITLE
# =========================

st.markdown(
    """
    <h1 style='text-align:center; font-size:70px;'>
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

st.markdown("<br><br>", unsafe_allow_html=True)

# =========================
# LOGIN FORM
# =========================

left, center, right = st.columns([2,3,2])

with center:

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
        