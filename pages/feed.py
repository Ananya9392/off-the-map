import streamlit as st
col1, col2 = st.columns([1,8])

with col1:
    if st.button("⬅"):
        st.switch_page("pages/home.py")

with col2:
 st.title("📰 Feed")

st.image("assets/beach.jpg")
st.write("Butterfly Beach")
st.write("Amazing hidden beach in Goa")
st.markdown("""
<style>

[data-testid="stSidebar"]{
    display:none;
}

</style>
""", unsafe_allow_html=True)

st.markdown("---")

st.image("assets/culture.jpg")
st.write("Cultural Experience")
st.write("Traditional festival in Assam")

st.markdown("---")

st.image("assets/market.jpg")
st.write("Hidden Market")
st.write("Local handmade products")





