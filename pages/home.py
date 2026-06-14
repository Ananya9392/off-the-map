import streamlit as st

if "wishlist" not in st.session_state:
    st.session_state.wishlist = []

st.set_page_config(
    page_title="Off The Map",
    page_icon="🗺️",
    layout="wide"
)
st.markdown("""
<style>

[data-testid="stSidebar"]{
    display:none;
}

</style>
""", unsafe_allow_html=True)

# ======================
# STYLING
# ======================

st.markdown("""
<style>
            
.glass-card{
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(20px);
    border:1px solid rgba(255,255,255,0.15);
    padding:20px;
    border-radius:25px;
}       

.stApp{
    background: linear-gradient(
        135deg,
        #0b132b,
        #1c2541,
        #3a506b,
        #5bc0be
    );
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

.stButton button{
    width:100%;
    border-radius:25px;
    background:rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.15);
    color:white;
    transition:0.3s;
}

.stButton button:hover{
    background:#00D4FF;
    color:black;
}

.stTextInput input{
    border-radius:20px;
    background:rgba(255,255,255,0.08);
    color:white;
}

img{
    border-radius:20px;
}

</style>
""", unsafe_allow_html=True)

# ======================
# LOGO
# ======================

st.markdown("""
<h1 style='
text-align:center;
font-size:70px;
font-weight:900;
color:#00D4FF;
'>
🧭 OFF THE MAP
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;color:#D8E2F0;'>
Beyond guidebooks. Beyond tourist traps.
</h3>
""", unsafe_allow_html=True)

# ======================
# SEARCH BAR
# ======================
search = st.text_input(
    "Search",
    label_visibility="collapsed",
    placeholder="Search hidden gems..."
)

st.markdown("---")

# ======================
# CATEGORIES
# ======================

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

posts = [
    {
        "name": "Butterfly Beach",
        "location": "Goa",
        "category": "Beach"
    },
    {
        "name": "Cultural Experience",
        "location": "Assam",
        "category": "Culture"
    },
    {
        "name": "Hidden Market",
        "location": "Ahmedabad",
        "category": "Shopping"
    }
]


st.markdown(
    "<h2 style='color:#FFB84D;'>🔥 Trending Hidden Gems</h2>",
    unsafe_allow_html=True
)

# ======================
# CARDS
# ======================

col1, col2, col3 = st.columns(3)

# ----------------------
# CARD 1
# ----------------------

with col1:

    st.image("assets/beach.jpg")
    st.markdown("### 📍 Butterfly Beach")
    st.write("🌊 Hidden Beach")
    st.write("📍 Goa, India")
    st.write("⭐⭐⭐⭐⭐")

    b1, b2, b3 = st.columns(3)

    with b1:
        st.button("❤️", key="goa_like")

    with b2:
        st.button("💬", key="goa_comment")

    with b3:
        if st.button("🔖", key="goa_save"):
            if "Butterfly Beach" not in st.session_state.wishlist:
                st.session_state.wishlist.append("Butterfly Beach")

    if st.button("View Details", key="goa"):
        st.switch_page("pages/Butterfly_Beach.py")


# ----------------------
# CARD 2
# ----------------------

with col2:

    st.image("assets/culture.jpg")
    st.markdown("### 🎭 Cultural Experience")
    st.write("🎉 Traditional Festival")
    st.write("📍 Assam, India")
    st.write("⭐⭐⭐⭐⭐")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.button("❤️", key="assam_like")

    with c2:
        st.button("💬", key="assam_comment")

    with c3:
        if st.button("🔖", key="assam_save"):
            if "Cultural Experience" not in st.session_state.wishlist:
                st.session_state.wishlist.append("Cultural Experience")

    if st.button("View Details", key="culture"):
        st.switch_page("pages/Cultural_Experience.py")


# ----------------------
# CARD 3
# ----------------------

with col3:

    st.image("assets/market.jpg")
    st.markdown("### 🛍 Hidden Market")
    st.write("🧵 Handmade Products")
    st.write("📍 Ahmedabad, India")
    st.write("⭐⭐⭐⭐")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.button("❤️", key="market_like")

    with m2:
        st.button("💬", key="market_comment")

    with m3:
        if st.button("🔖", key="market_save"):
            if "Hidden Market" not in st.session_state.wishlist:
                st.session_state.wishlist.append("Hidden Market")

    if st.button("View Details", key="market"):
        st.switch_page("pages/Hidden_Market.py")

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
        






        
