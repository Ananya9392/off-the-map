import streamlit as st
import base64

st.set_page_config(
    page_title="Subscriptions",
    page_icon="💎",
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

    .plan-card {{
        background:rgba(255,255,255,0.92);
        border-radius:25px;
        padding:20px;
        min-height:260px;
        margin-bottom:20px;
        box-shadow:0px 8px 20px rgba(0,0,0,0.15);
        text-align:center;
    }}

    .price {{
        color:#008000;
        font-size:30px;
        font-weight:bold;
    }}

    .stButton button {{
        width:100%;
        border-radius:15px;
        height:45px;
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
    st.title("💎 Premium Subscriptions")

st.markdown(
    """
    ### Unlock premium travel recommendations and discover hidden gems before everyone else.
    """
)

st.markdown("---")

# ==========================
# SHORT TERM
# ==========================

st.subheader("⚡ Short Term Plans")

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(
        """
        <div class="plan-card">
        <h2 style="color:black;">3 Days</h2>
        <div class="price">₹49</div>
        <p style="color:black;">
        Perfect for weekend trips and quick adventures.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Choose 3 Days"):
        st.success("3 Days Plan Selected")

with c2:

    st.markdown(
        """
        <div class="plan-card">
        <h2 style="color:black;">5 Days</h2>
        <div class="price">₹79</div>
        <p style="color:black;">
        Great for short vacations and city explorations.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Choose 5 Days"):
        st.success("5 Days Plan Selected")

with c3:

    st.markdown(
        """
        <div class="plan-card">
        <h2 style="color:black;">1 Week</h2>
        <div class="price">₹99</div>
        <p style="color:black;">
        Discover more destinations at your own pace.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Choose 1 Week"):
        st.success("1 Week Plan Selected")

st.markdown("<br>", unsafe_allow_html=True)

# ==========================
# LONG TERM
# ==========================

st.subheader("🌍 Long Term Plans")

c4, c5, c6, c7 = st.columns(4)

with c4:

    st.markdown(
        """
        <div class="plan-card">
        <h2 style="color:black;">1 Month</h2>
        <div class="price">₹199</div>
        <p style="color:black;">
        Perfect for regular travelers.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Choose 1 Month"):
        st.success("1 Month Plan Selected")

with c5:

    st.markdown(
        """
        <div class="plan-card">
        <h2 style="color:black;">3 Months</h2>
        <div class="price">₹499</div>
        <p style="color:black;">
        Extended access to premium travel content.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Choose 3 Months"):
        st.success("3 Months Plan Selected")

with c6:

    st.markdown(
        """
        <div class="plan-card">
        <h2 style="color:black;">6 Months</h2>
        <div class="price">₹899</div>
        <p style="color:black;">
        Best value for travel enthusiasts.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Choose 6 Months"):
        st.success("6 Months Plan Selected")

with c7:

    st.markdown(
        """
        <div class="plan-card">
        <h2 style="color:black;">12 Months</h2>
        <div class="price">₹1499</div>
        <p style="color:black;">
        Full-year premium access and exclusive discoveries.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Choose 12 Months"):
        st.success("12 Months Plan Selected")

st.markdown("---")

st.info(
    "🚀 Payment integration can be added later using Razorpay, Stripe, or PayPal."
)
