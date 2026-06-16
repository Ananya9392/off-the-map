import streamlit as st
import base64
import json

# ==========================
# PAGE CONFIG
# ==========================

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
# CURRENT USER POSTS ONLY
# ==========================

current_user_email = st.session_state.get(
    "email",
    ""
)

user_posts = []

for post in posts:

    if (
        post.get("user_post", False)
        and post.get("owner_email", "") == current_user_email
    ):
        user_posts.append(post)

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

    h1,h2,h3,h4,h5,h6,label {{
        color:white !important;
    }}

    .stat-card {{
        background:rgba(255,255,255,0.15);
        backdrop-filter:blur(15px);
        padding:20px;
        border-radius:20px;
        text-align:center;
    }}

    .post-card {{
        background:rgba(255,255,255,0.92);
        border-radius:20px;
        padding:20px;
        margin-top:10px;
        margin-bottom:20px;
        box-shadow:0px 5px 15px rgba(0,0,0,0.2);
    }}

    .post-card h1,
    .post-card h2,
    .post-card h3,
    .post-card h4,
    .post-card h5,
    .post-card h6,
    .post-card p,
    .post-card div,
    .post-card span {{
        color:black !important;
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
            <div class="post-card">

            <h3>
            📍 {post['title']}
            </h3>

            <p>
            📌 {post['location']}
            </p>

            <p>
            🏷 {post['category']}
            </p>

            <p>
            {post['description']}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "🗑 Delete Post",
            key=f"delete_{post['title']}"
        ):

            try:

                with open(
                    "data/posts.json",
                    "r"
                ) as f:

                    all_posts = json.load(f)

                updated_posts = []

                for p in all_posts:

                    if (
                        p.get("owner_email") == current_user_email
                        and p.get("title") == post["title"]
                    ):
                        continue

                    updated_posts.append(p)

                with open(
                    "data/posts.json",
                    "w"
                ) as f:

                    json.dump(
                        updated_posts,
                        f,
                        indent=4
                    )

                st.cache_data.clear()

                st.success(
                    "Post deleted successfully!"
                )

                st.rerun()

            except Exception as e:

                st.error(
                    f"Error deleting post: {e}"
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
