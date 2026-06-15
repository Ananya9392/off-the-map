import streamlit as st
import base64
import json

st.set_page_config(
    page_title="Feed",
    page_icon="📰",
    layout="wide"
)

# ==========================
# SESSION STATE
# ==========================

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

# ==========================
# LOAD POSTS
# ==========================

try:
    with open("data/posts.json", "r") as f:
        posts = json.load(f)
except:
    posts = []

# ==========================
# BACKGROUND
# ==========================

with open("assets/mountains.jpg", "rb") as image:
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
    st.title("📰 Feed")

st.markdown("---")

# ==========================
# INSTAGRAM STYLE FEED
# ==========================

for index, post in enumerate(reversed(posts)):

    st.markdown(
        f"""
        ### 📍 {post['title']}
        """
    )

    st.caption(
        f"📌 {post['location']} • 🏷 {post['category']}"
    )

    st.image(
        post["image"],
        width=450
    )

    st.write(post["description"])

    a, b, c = st.columns(3)

    with a:
        st.button(
            "❤️",
            key=f"like_{index}"
        )

    with b:
        st.button(
            "💬",
            key=f"comment_{index}"
        )

    with c:

        if st.button(
            "🔖",
            key=f"save_{index}"
        ):

            exists = False

            for item in st.session_state.wishlist:
                if item["title"] == post["title"]:
                    exists = True

            if not exists:
                st.session_state.wishlist.append(post)
                st.success("Added to Wishlist")

    st.markdown("---")
    
