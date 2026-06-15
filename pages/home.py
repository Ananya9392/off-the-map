import streamlit as st
import base64

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="Off The Map",
    page_icon="🗺️",
    layout="wide"
)

# -------------------------
# SESSION STATE
# -------------------------

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

# -------------------------
# BACKGROUND
# -------------------------

def set_bg(image_file):

    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

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

        .stButton button {{
            width:100%;
            border-radius:20px;
        }}

        img {{
            border-radius:20px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("assets/mountains.jpg")

# -------------------------
# TITLE
# -------------------------

st.markdown("""
<h1 style='text-align:center;font-size:70px;'>
🧭 OFF THE MAP
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;'>
Beyond guidebooks. Beyond tourist traps.
</h3>
""", unsafe_allow_html=True)

# -------------------------
# SEARCH
# -------------------------

search = st.text_input(
    "",
    placeholder="Search hidden gems..."
)

st.markdown("---")

# -------------------------
# CATEGORIES
# -------------------------

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.button("🏖 Beaches")

with c2:
    st.button("🍜 Food")

with c3:
    st.button("🎭 Culture")

with c4:
    st.button("🛍 Shopping")

with c5:
    st.button("🌿 Nature")

st.markdown("---")

# -------------------------
# TRENDING
# -------------------------

st.subheader("🔥 Trending Hidden Gems")

col1, col2, col3 = st.columns(3)

# ==================================
# BUTTERFLY BEACH
# ==================================

with col1:

    st.image("assets/beach.jpg")

    st.markdown("### 📍 Butterfly Beach")
    st.write("🌊 Hidden Beach")
    st.write("📍 Goa, India")
    st.write("⭐⭐⭐⭐⭐")

    a, b, c = st.columns(3)

    with a:
        st.button("❤️", key="beach_like")

    with b:
        st.button("💬", key="beach_comment")

    with c:
        if st.button("🔖", key="beach_save"):

            if "Butterfly Beach" not in st.session_state.wishlist:
                st.session_state.wishlist.append(
                    "Butterfly Beach"
                )

    if st.button("View Details", key="beach_details"):
        st.switch_page("pages/Butterfly_Beach.py")

# ==================================
# CULTURAL EXPERIENCE
# ==================================

with col2:

    st.image("assets/culture.jpg")

    st.markdown("### 🎭 Cultural Experience")
    st.write("🎉 Traditional Festival")
    st.write("📍 Assam, India")
    st.write("⭐⭐⭐⭐⭐")

    a, b, c = st.columns(3)

    with a:
        st.button("❤️", key="culture_like")

    with b:
        st.button("💬", key="culture_comment")

    with c:
        if st.button("🔖", key="culture_save"):

            if "Cultural Experience" not in st.session_state.wishlist:
                st.session_state.wishlist.append(
                    "Cultural Experience"
                )

    if st.button("View Details", key="culture_details"):
        st.switch_page("pages/Cultural_Experience.py")

# ==================================
# HIDDEN MARKET
# ==================================

with col3:

    st.image("assets/market.jpg")

    st.markdown("### 🛍 Hidden Market")
    st.write("🧵 Handmade Products")
    st.write("📍 Ahmedabad, India")
    st.write("⭐⭐⭐⭐")

    a, b, c = st.columns(3)

    with a:
        st.button("❤️", key="market_like")

    with b:
        st.button("💬", key="market_comment")

    with c:
        if st.button("🔖", key="market_save"):

            if "Hidden Market" not in st.session_state.wishlist:
                st.session_state.wishlist.append(
                    "Hidden Market"
                )

    if st.button("View Details", key="market_details"):
        st.switch_page("pages/Hidden_Market.py")

# -------------------------
# BOTTOM NAVIGATION
# -------------------------

st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")

n1, n2, n3, n4 = st.columns(4)

with n1:
    if st.button("👤 Profile"):
        st.switch_page("pages/profile.py")

with n2:
    if st.button("🔖 Wishlist"):
        st.switch_page("pages/wishlist.py")

with n3:
    if st.button("➕ Post"):
        st.switch_page("pages/add_place.py")

with n4:
    if st.button("📰 Feed"):
        st.switch_page("pages/feed.py")
        