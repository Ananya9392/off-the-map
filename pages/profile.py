import streamlit as st
import base64

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)

# =====================
# BACKGROUND IMAGE
# =====================

with open("assets/profile_bg.jpg", "rb") as image:
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
        display: none;
    }}

    .profile-card {{
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(20px);
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(255,255,255,0.2);
    }}

    h1, h2, h3, h4, h5, h6, p, label {{
        color: white !important;
    }}

    .stButton button {{
        width: 100%;
        border-radius: 20px;
        background: rgba(255,255,255,0.15);
        color: white;
        border: 1px solid rgba(255,255,255,0.2);
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =====================
# BACK BUTTON
# =====================

col1, col2 = st.columns([1, 8])

with col1:
    if st.button("⬅"):
        st.switch_page("pages/home.py")

with col2:
    st.title("👤 My Profile")

st.markdown("<br>", unsafe_allow_html=True)

# =====================
# PROFILE CARD
# =====================

st.markdown('<div class="profile-card">', unsafe_allow_html=True)

st.subheader("Personal Information")

name = st.session_state.get("name", "Ananya")
email = st.session_state.get("email", "ananya@email.com")
phone = st.session_state.get("phone", "+91 XXXXX XXXXX")

st.write(f"👤 Name: {name}")
st.write(f"📧 Email: {email}")
st.write(f"📱 Phone: {phone}")

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================
# ACTION BUTTONS
# =====================

c1, c2 = st.columns(2)

with c1:
    st.button("✏️ Edit Profile")

with c2:
    st.button("⚙️ Settings")
    