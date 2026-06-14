import streamlit as st

st.set_page_config(
    page_title="Off The Map",
    page_icon="🗺️",
    layout="wide"
)

# ======================
# STYLING
# ======================

st.markdown("""
<style>

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

st.text_input(
    "Search",
    label_visibility="collapsed",
    placeholder="Search..."
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

st.markdown(
    "<h2 style='color:#FFB84D;'>🔥 Trending Hidden Gems</h2>",
    unsafe_allow_html=True
)

# ======================
# CARDS
# ======================

col1, col2, col3 = st.columns(3)

with col1:
    st.image("assets/beach.jpg")
    st.markdown("### 📍 Butterfly Beach")
    st.write("🌊 Hidden Beach")
    st.write("📍 Goa, India")
    st.write("⭐⭐⭐⭐⭐")

    if st.button("View Details", key="goa"):
        st.switch_page("pages/Butterfly_Beach.py")

with col2:
    st.image("assets/culture.jpg")
    st.markdown("### 🎭 Cultural Experience")
    st.write("🎉 Traditional Festival")
    st.write("📍 Assam, India")
    st.write("⭐⭐⭐⭐⭐")

    if st.button("View Details", key="culture"):
        st.switch_page("pages/Cultural_Experience.py")

with col3:
    st.image("assets/market.jpg")
    st.markdown("### 🛍 Hidden Market")
    st.write("🧵 Handmade Products")
    st.write("📍 Ahmedabad, India")
    st.write("⭐⭐⭐⭐")

    if st.button("View Details", key="market"):
        st.switch_page("pages/Hidden_Market.py")
