import streamlit as st
import base64

st.set_page_config(
    page_title="Bucket List",
    page_icon="🪣",
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

with open("assets/background.jpg", "rb") as image:
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
    st.title("🪣 My Bucket List")

st.markdown("---")

# ==========================
# EMPTY LIST
# ==========================

if len(st.session_state.wishlist) == 0:

    st.info(
        "No places added to your Bucket List yet."
    )

# ==========================
# POSTS
# ==========================

else:

    cols = st.columns(2)

    for index, post in enumerate(
        st.session_state.wishlist
    ):

        with cols[index % 2]:

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

            if st.button(
                "❌ Remove",
                key=f"remove_{index}"
            ):
                st.session_state.wishlist.pop(index)
                st.rerun()

            st.markdown("<br>", unsafe_allow_html=True)
            