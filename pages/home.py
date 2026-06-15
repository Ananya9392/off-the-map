import streamlit as st
import base64
import json

# ==========================
# PAGE CONFIG
# ==========================

st.set_page_config(
    page_title="Off The Map",
    page_icon="🧭",
    layout="wide"
)

# ==========================
# SESSION STATE
# ==========================

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

if "selected_category" not in st.session_state:
    st.session_state.selected_category = "All"

# ==========================
# LOAD POSTS
# ==========================

with open("data/posts.json", "r") as f:
    posts = json.load(f)

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
# TITLE
# ==========================

st.markdown(
    """
    <h1 style='text-align:center;font-size:65px;'>
    🧭 OFF THE MAP
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

st.markdown("---")

# ==========================
# SEARCH
# ==========================

search = st.text_input(
    "",
    placeholder="🔍 Search hidden gems..."
)

# ==========================
# CATEGORY BUTTONS
# ==========================

c1, c2, c3, c4, c5, c6 = st.columns(6)

with c1:
    if st.button("All"):
        st.session_state.selected_category = "All"

with c2:
    if st.button("🏖 Beach"):
        st.session_state.selected_category = "Beach"

with c3:
    if st.button("🍜 Food"):
        st.session_state.selected_category = "Food"

with c4:
    if st.button("🎭 Culture"):
        st.session_state.selected_category = "Culture"

with c5:
    if st.button("🛍 Shopping"):
        st.session_state.selected_category = "Shopping"

with c6:
    if st.button("🌿 Nature"):
        st.session_state.selected_category = "Nature"

selected_category = st.session_state.selected_category

st.markdown("---")

# ==========================
# TRENDING POSTS ONLY
# ==========================

filtered_posts = []

for post in posts:

    # Skip user uploaded posts
    if post.get("user_post", False):
        continue

    search_match = (
        search.lower() in post["title"].lower()
        or search.lower() in post["location"].lower()
    )

    category_match = (
        selected_category == "All"
        or post["category"] == selected_category
    )

    if search_match and category_match:
        filtered_posts.append(post)

# ==========================
# TRENDING SECTION
# ==========================

st.subheader("🔥 Trending Hidden Gems")

cols = st.columns(3)

for index, post in enumerate(filtered_posts):

    with cols[index % 3]:

        st.image(
            post["image"],
            width=250
        )

        with st.container():

            st.markdown(
                f"""
                ### {post["title"]}
                """
            )

            st.write(f"📍 {post['location']}")
            st.write(f"🏷 {post['category']}")
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

        if st.button(
            "View Details",
            key=f"details_{index}"
        ):

            if post["title"] == "Butterfly Beach":
                st.switch_page("pages/Butterfly_Beach.py")

            elif post["title"] == "Cultural Experience":
                st.switch_page("pages/Cultural_Experience.py")

            elif post["title"] == "Hidden Market":
                st.switch_page("pages/Hidden_Market.py")

# ==========================
# BOTTOM NAVIGATION
# ==========================

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")

nav1, nav2, nav3, nav4 = st.columns(4)

with nav1:
    if st.button("👤 Profile"):
        st.switch_page("pages/profile.py")

with nav2:
    if st.button("🔖 Wishlist"):
        st.switch_page("pages/wishlist.py")

with nav3:
    if st.button("➕ Post"):
        st.switch_page("pages/add_place.py")

with nav4:
    if st.button("📰 Feed"):
        st.switch_page("pages/feed.py")
        
