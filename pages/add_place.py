import streamlit as st
import base64

st.set_page_config(
    page_title="Add Place",
    page_icon="➕",
    layout="wide"
)

# =====================
# BACKGROUND IMAGE
# =====================

with open("assets/mountains.jpg", "rb") as image:
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

    [data-testid="stSidebar"] {{
        display:none;
    }}

    h1,h2,h3,h4,h5,h6,p,label {{
        color:white !important;
    }}

    .form-card {{
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(20px);
        padding: 25px;
        border-radius: 25px;
        border: 1px solid rgba(255,255,255,0.2);
    }}

    .stButton button {{
        width:100%;
        border-radius:20px;
        background:rgba(255,255,255,0.15);
        border:1px solid rgba(255,255,255,0.2);
        color:white;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =====================
# HEADER
# =====================

col1, col2 = st.columns([1,8])

with col1:
    if st.button("⬅"):
        st.switch_page("pages/home.py")

with col2:
    st.title("➕ Add Place")

st.markdown("<br>", unsafe_allow_html=True)

# =====================
# FORM
# =====================

st.markdown('<div class="form-card">', unsafe_allow_html=True)

place = st.text_input("📍 Place Name")

category = st.selectbox(
    "🏷 Category",
    ["Beach", "Food", "Culture", "Shopping", "Nature"]
)

location = st.text_input("📌 Location")

description = st.text_area(
    "📝 What makes it special?"
)

rating = st.slider(
    "⭐ Rating",
    1,
    5
)

image = st.file_uploader(
    "📷 Upload Image"
)

if st.button("🚀 Post"):
    st.success("Post Uploaded Successfully!")

st.markdown("</div>", unsafe_allow_html=True)
