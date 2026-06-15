import streamlit as st
import time

st.set_page_config(
    page_title="Off The Map",
    page_icon="🧭",
    layout="wide"
)

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

.title{
    text-align:center;
    font-size:80px;
    font-weight:900;
    color:white;
    margin-top:250px;
}

.tagline{
    text-align:center;
    color:#D8E2F0;
    font-size:24px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='title'>🧭 OFF THE MAP</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='tagline'>Discover places tourists never find</div>",
    unsafe_allow_html=True
)

time.sleep(3)

st.switch_page("pages/login.py")



        