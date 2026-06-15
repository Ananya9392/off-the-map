import streamlit as st
import base64
import json

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)

# ==========================
# LOAD POSTS
# ==========================

try:
    with open("data/posts.json", "r") as f:
        posts = json.load(f)
except:
    posts = []

# ==========================
# COUNT USER POSTS ONLY
# ==========================

user_posts = 0

for post in posts:
    if post.get("user_post", False):
        user_posts += 1

# ==========================
# SESSION STATE
# ==========================

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

if "name" not in st.session_state:
    st.session_state.name = "Guest User"

if "email" not in st.session_state:
    st.session_state.email = ""

if "phone" not in st.session_state:
    st.session_state.phone = ""

# ==========================
# BACKGROUND
# ==========================

with open("assets/profile_bg.jpg", "rb") as image:
    encoded = base64.b64encode(image.read()).decode()

st.markdown(
    f"""
    <style>

    .stApp {{
        background-image:url("data:image/jpg;base64,{encoded}");
        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;
        background-attachment:fixed;
    }}

    [data-testid="stSidebar"] {{
        display:none;
    }}

    h1,h2,h3,h4,h5,h6,p,label {{
        color:white !important;
    }}

    .profile-card {{
        background:rgba(255,255,255,0.15);
        backdrop-filter:blur(20px);
        padding:30px;
        border-radius:25px;
        border:1px solid rgba(255,255,255,0.2);
    }}

    .stat-card {{
        background:rgba(255,255,255,0.15);
        backdrop-filter:blur(15px);
        padding:20px;
        border-radius:20px;
        text-align:center;
    }}

    .stButton button {{
        width:100%;
        border-radius:15px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ==========================
# HEADER
# ==========================

col1, col2 = st.columns([1,8])

with col1:
    if st.button("⬅"):
        st.switch_page("pages/home.py")

with col2:
    st.title("👤 My Profile")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================
# PROFILE SECTION
# ==========================

st.markdown(
    """
    <div class="profile-card">
    <h2>Personal Information</h2>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

name = st.text_input(
    "👤 Name",
    value=st.session_state.name
)

email = st.text_input(
    "📧 Email",
    value=st.session_state.email
)

phone = st.text_input(
    "📱 Phone",
    value=st.session_state.phone
)

if st.button("💾 Save Changes"):

    st.session_state.name = name
    st.session_state.email = email
    st.session_state.phone = phone

    st.success("Profile Updated Successfully!")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================
# STATS
# ==========================

c1, c2 = st.columns(2)

with c1:

    st.markdown(
        f"""
        <div class="stat-card">
        <h2>{len(st.session_state.wishlist)}</h2>
        <p>Saved Places</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        f"""
        <div class="stat-card">
        <h2>{user_posts}</h2>
        <p>Your Posts</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================
# RECENT USER POSTS
# ==========================

st.subheader("📝 Your Posts")

found = False

for post in posts:

    if post.get("user_post", False):

        found = True

        st.write(f"📍 {post['title']}")
        st.write(f"📌 {post['location']}")
        st.write(f"🏷 {post['category']}")
        st.markdown("---")

if not found:
    st.info("You haven't uploaded any posts yet.")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================
# LOGOUT
# ==========================

if st.button("🚪 Logout"):

    st.session_state.clear()

    st.switch_page("pages/login.py")
    