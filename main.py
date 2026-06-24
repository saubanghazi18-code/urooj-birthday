import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Happy 16th Birthday Urooj Fatima 🎀",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Cute Pink Elegant Theme
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffe4f0 0%, #f8d7e8 100%);
    }
    .main-title {
        font-size: 58px;
        font-weight: 700;
        color: #d81b60;
        text-align: center;
        margin-bottom: 8px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .subtitle {
        font-size: 32px;
        color: #ad1457;
        text-align: center;
        font-weight: 500;
        margin-bottom: 30px;
    }
    .message {
        font-size: 24px;
        line-height: 1.75;
        color: #4a2c4f;
        text-align: center;
        max-width: 720px;
        margin: 35px auto;
        background: rgba(255,255,255,0.75);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .highlight {
        color: #e91e63;
        font-weight: 600;
    }
    .button {
        background-color: #ff69b4;
        color: white;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-title">Happy Sweet 16 ✨</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Urooj Fatima 🎀</p>', unsafe_allow_html=True)

# Main Message
st.markdown("""
    <p class="message">
        Dear Urooj,<br><br>
        
        Happy 16th Birthday! 🎉🌸<br><br>
        
        You’ve grown into such a beautiful, smart, and amazing young woman. 
        As your cousin who sees you like a little sister, I’m really proud of everything you are and everything you’re becoming.<br><br>
        
        May your 16th year be filled with joy, success, new adventures, and all the things that make you happy. 
        Keep shining brightly and following your dreams — the world is yours.<br><br>
        
        I’m always here for you, no matter what. 
        Wishing you the most beautiful and memorable Sweet 16!
    </p>
""", unsafe_allow_html=True)

# Cute Interactive Elements
st.markdown("### 💕 Make Your Birthday Special")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌸 Send a Virtual Hug", use_container_width=True):
        st.success("Hug delivered with lots of love 🤗💕")
        st.balloons()

with col2:
    if st.button("🎂 Blow the Candles", use_container_width=True):
        st.balloons()
        st.success("Wish granted! ✨ Make another one!")

with col3:
    if st.button("💖 Heart Sparkles", use_container_width=True):
        st.snow()
        st.success("Sparkles and good vibes sent! 🌟")

# Extra cute touches
st.markdown("---")
st.markdown("""
    <p style='text-align: center; font-size: 22px; color: #c2185b;'>
        Lots of love & pride ❤️
    </p>
""", unsafe_allow_html=True)

st.caption(f"From your big cousin • {datetime.now().strftime('%B %d, %Y')}")

# Floating balloons effect
st.balloons()
