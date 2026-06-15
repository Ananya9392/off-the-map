import streamlit as st
import base64

st.set_page_config(
    page_title="Wishlist",
    page_icon="🔖",
    layout="wide"
)

# ==========================
# SESSION STATE
# ==========================

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

# ==========================
# BACKGROUND
# ==========================

with open("assets/wishlist_bg.jpg", "rb") as image:
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
        border-radius:15px;
        width:100%;
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
    st.title("🔖 My Wishlist")

st.markdown("---")

# ==========================
# EMPTY WISHLIST
# ==========================

if len(st.session_state.wishlist) == 0:

    st.info("No saved places yet.")

# ==========================
# WISHLIST POSTS
# ==========================

else:

    cols = st.columns(2)

    for index, post in enumerate(st.session_state.wishlist):

        with cols[index % 2]:

            st.image(
                post["image"],
                width=250
            )

            st.markdown(
                f"""
                ### 📍 {post['title']}
                """
            )

            st.write(f"📌 {post['location']}")
            st.write(f"🏷 {post['category']}")
            st.write(post['description'])

            if st.button(
                "❌ Remove",
                key=f"remove_{index}"
            ):
                st.session_state.wishlist.pop(index)
                st.rerun()

            st.markdown("---")
            