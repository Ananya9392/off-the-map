import streamlit as st

if st.button("⬅ Back"):
    st.switch_page("pages/home.py")

st.title("📍 Butterfly Beach")

st.image("assets/beach.jpg")

st.subheader("About")

st.write("""
A peaceful hidden beach in Goa known for
beautiful sunsets and fewer tourists.
""")

st.subheader("Posted By")

st.write("Ananya")

st.subheader("Best Time To Visit")

st.write("November to February")

st.subheader("Travel Tips")

st.write("""
• Visit before sunset

• Carry water

• Wear comfortable shoes
""")

