import streamlit as st
import base64

st.set_page_config(
    page_title="Wishlist",
    page_icon="🔖",
    layout="wide"
)

# =====================
# BACKGROUND IMAGE
# =====================

with open("assets/wishlist_bg.jpg", "rb") as image:
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

    .wishlist-card {{
        background: rgba(255,255,255,0.15);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 20px;
        padding: 20px;
        margin-bottom: 15px;
        color: white;
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
# SESSION STATE
# =====================

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

# =====================
# HEADER
# =====================

col1, col2 = st.columns([1,8])

with col1:
    if st.button("⬅"):
        st.switch_page("pages/home.py")

with col2:
    st.title("🔖 My Wishlist")

st.markdown("<br>", unsafe_allow_html=True)

# =====================
# WISHLIST ITEMS
# =====================

if len(st.session_state.wishlist) == 0:

    st.info("No saved places yet.")

else:

    for place in st.session_state.wishlist:

        st.markdown(
            f"""
            <div class="wishlist-card">
                <h3>📍 {place}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        