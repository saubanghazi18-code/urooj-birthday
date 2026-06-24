import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Happy 16th Birthday Urooj Fatima 🎀",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Cute Pink + Purple Theme + Floating Hearts
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffe4f0 0%, #f3d8ff 100%);
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
        color: #9c27b0;
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
        background: rgba(255,255,255,0.85);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    /* Floating Purple Hearts */
    @keyframes floatUp {
        0% { transform: translateY(100px) scale(0.5); opacity: 0; }
        20% { opacity: 1; }
        80% { opacity: 1; }
        100% { transform: translateY(-800px) scale(1.2); opacity: 0; }
    }
    .floating-heart {
        position: fixed;
        font-size: 35px;
        animation: floatUp 6s linear forwards;
        z-index: 1000;
        pointer-events: none;
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
        As your cousin who sees you like a little sister, I’m really proud of you.<br><br>
        
        May your 16th year be filled with joy, success, new adventures, and all the happiness you deserve. 
        Keep shining and chasing your dreams.<br><br>
        
        I’m always here for you. Wishing you a truly memorable Sweet 16!
    </p>
""", unsafe_allow_html=True)

# Interactive Section
st.markdown("### 💜 Celebrate with Floating Hearts")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌸 Send a Virtual Hug", use_container_width=True):
        st.success("Hug sent with love 🤗💕")
        st.markdown(create_floating_hearts(8), unsafe_allow_html=True)

with col2:
    if st.button("🎂 Blow the Candles", use_container_width=True):
        st.success("Wish granted! ✨")
        st.markdown(create_floating_hearts(10), unsafe_allow_html=True)

with col3:
    if st.button("💜 Purple Heart Blast", use_container_width=True):
        st.success("Hearts floating your way! 💜")
        st.markdown(create_floating_hearts(15), unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <p style='text-align: center; font-size: 22px; color: #9c27b0;'>
        Lots of love & pride from your big cousin ❤️
    </p>
""", unsafe_allow_html=True)

st.caption(f"Sent on {datetime.now().strftime('%B %d, %Y')}")

# Helper function for floating hearts
def create_floating_hearts(count=10):
    hearts = ""
    for i in range(count):
        left = random.randint(10, 90)
        delay = random.uniform(0.2, 2.5)
        size = random.randint(25, 45)
        hearts += f"""
            <span class="floating-heart" 
                  style="left: {left}%; 
                         animation-delay: {delay}s;
                         font-size: {size}px;">
                💜
            </span>
        """
    return hearts
