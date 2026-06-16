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

@st.cache_data
def load_posts():
    try:
        with open("data/posts.json", "r") as f:
            return json.load(f)
    except:
        return []

posts = load_posts()

# ==========================
# USER POSTS ONLY
# ==========================

user_posts = []

for post in posts:

    if post.get("user_post", False):

        user_posts.append(post)

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

    .stat-card {{
        background:rgba(255,255,255,0.15);
        backdrop-filter:blur(15px);
        padding:20px;
        border-radius:20px;
        text-align:center;
    }}

    .info-card {{
        background:rgba(255,255,255,0.92);
        padding:18px;
        border-radius:20px;
        margin-top:10px;
        margin-bottom:10px;
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
# PROFILE INFO
# ==========================

st.subheader("Personal Information")

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

    st.success(
        "Profile Updated Successfully!"
    )

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
        <p>Bucket List</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        f"""
        <div class="stat-card">
        <h2>{len(user_posts)}</h2>
        <p>Your Posts</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================
# USER POSTS
# ==========================

st.subheader("📝 Your Uploaded Posts")

if len(user_posts) == 0:

    st.info(
        "You haven't uploaded any posts yet."
    )

else:

    for post in reversed(user_posts):

        st.image(
            post["image"],
            width=220
        )

        st.markdown(
            f"""
            <div class="info-card">

            <h3 style="color:black;">
            📍 {post['title']}
            </h3>

            <p style="color:black;">
            📌 {post['location']}
            </p>

            <p style="color:black;">
            🏷 {post['category']}
            </p>

            <p style="color:black;">
            {post['description']}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

# ==========================
# LOGOUT
# ==========================

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚪 Logout"):

    st.session_state.clear()

    st.switch_page(
        "pages/login.py"
    )
    