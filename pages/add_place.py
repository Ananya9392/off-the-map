import streamlit as st
import base64
import json
import os
from datetime import datetime

st.set_page_config(
    page_title="Add Place",
    page_icon="➕",
    layout="wide"
)

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

    .stButton button {{
        width:100%;
        border-radius:15px;
        height:50px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# ==========================
# USER INFO
# ==========================

user_name = st.session_state.get(
    "name",
    "Guest User"
)

user_email = st.session_state.get(
    "email",
    "unknown@email.com"
)

# ==========================
# HEADER
# ==========================

col1, col2 = st.columns([1,8])

with col1:
    if st.button("⬅"):
        st.switch_page("pages/home.py")

with col2:
    st.title("➕ Add Hidden Gem")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================
# CENTERED FORM
# ==========================

left, center, right = st.columns([1,2,1])

with center:

    place = st.text_input(
        "📍 Place Name"
    )

    category = st.selectbox(
        "🏷 Category",
        [
            "Beach",
            "Food",
            "Culture",
            "Shopping",
            "Nature"
        ]
    )

    location = st.text_input(
        "📌 Location"
    )

    description = st.text_area(
        "📝 Description"
    )

    image = st.file_uploader(
        "📷 Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Post Hidden Gem"):

        if (
            place.strip() == ""
            or location.strip() == ""
            or description.strip() == ""
            or image is None
        ):

            st.error(
                "Please complete all fields."
            )

        else:

            os.makedirs(
                "assets/uploads",
                exist_ok=True
            )

            image_path = (
                f"assets/uploads/{image.name}"
            )

            with open(
                image_path,
                "wb"
            ) as f:

                f.write(
                    image.getbuffer()
                )

            try:

                with open(
                    "data/posts.json",
                    "r"
                ) as f:

                    posts = json.load(f)

            except:

                posts = []

            new_post = {

                "title": place,
                "category": category,
                "location": location,
                "description": description,
                "image": image_path,

                "user_post": True,

                "owner_name": user_name,
                "owner_email": user_email,

                "timestamp": datetime.now().strftime(
                    "%d %b %Y %I:%M %p"
                )
            }

            posts.append(new_post)

            with open(
                "data/posts.json",
                "w"
            ) as f:

                json.dump(
                    posts,
                    f,
                    indent=4
                )

            st.success(
                "Hidden Gem Uploaded Successfully!"
            )

            st.balloons()

            st.switch_page(
                "pages/feed.py"
            )
            