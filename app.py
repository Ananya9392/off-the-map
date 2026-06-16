import streamlit as st
import time
import base64

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Off The Map",
    page_icon="🧭",
    layout="wide"
)

# ==========================
# BACKGROUND
# ==========================

with open("assets/background.jpg", "rb") as image:
    encoded = base64.b64encode(image.read()).decode()

st.markdown(
    f"""
    <style>

    .stApp {{
        background-image:url("data:image/jpg;base64,{encoded}");
        background-size:cover;
        background-position:center center;
        background-repeat:no-repeat;
        background-attachment:fixed;
    }}

    [data-testid="stSidebar"] {{
        display:none;
    }}

    .title {{
        text-align:center;
        font-size:75px;
        font-weight:900;
        color:white;
        margin-top:10px;
    }}

    .tagline {{
        text-align:center;
        color:white;
        font-size:26px;
        font-weight:500;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ==========================
# SPACING
# ==========================

st.markdown("<br><br><br>", unsafe_allow_html=True)

# ==========================
# CENTER LOGO
# ==========================

left, center, right = st.columns([2,1,2])

with center:
    st.image(
        "assets/logo.jpg",
        width=220
    )

# ==========================
# TITLE
# ==========================

st.markdown(
    """
    <div class="title">
    OFF THE MAP
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="tagline">
    Discover Hidden Gems Around The World
    </div>
    """,
    unsafe_allow_html=True
)

# ==========================
# SPLASH DELAY
# ==========================

time.sleep(3)

st.switch_page("pages/login.py")
