import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Happy 16th Birthday Urooj Fatima 🎀",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Cute Pink + Purple Theme with Heart Animation
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
        background: rgba(255,255,255,0.8);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    /* Purple Heart Animation */
    @keyframes heartPop {
        0% { transform: scale(0.2); opacity: 0; }
        50% { transform: scale(1.3); }
        100% { transform: scale(1); opacity: 1; }
    }
    .heart {
        font-size: 40px;
        animation: heartPop 1.5s ease forwards;
        display: inline-block;
        margin: 5px;
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
        Keep shining brightly and following your dreams.<br><br>
        
        I’m always here for you. Wishing you the most beautiful and memorable Sweet 16!
    </p>
""", unsafe_allow_html=True)

# Interactive Section with Purple Hearts
st.markdown("### 💜 Make Your Birthday Magical")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🌸 Send a Virtual Hug", use_container_width=True):
        st.success("Hug delivered with love 🤗💕")
        st.markdown("""
            <div style="text-align:center; margin:20px 0;">
                <span class="heart">💜</span>
                <span class="heart">💜</span>
                <span class="heart">💜</span>
                <span class="heart">💜</span>
                <span class="heart">💜</span>
            </div>
        """, unsafe_allow_html=True)

with col2:
    if st.button("🎂 Blow the Candles", use_container_width=True):
        st.success("Wish granted! ✨")
        st.markdown("""
            <div style="text-align:center; margin:20px 0;">
                💜💜💜💜💜💜💜
            </div>
        """, unsafe_allow_html=True)

with col3:
    if st.button("💜 Purple Heart Blast", use_container_width=True):
        st.markdown("""
            <div style="text-align:center; margin:25px 0; font-size:50px;">
                💜 💜 💜 💜 💜<br>
                💜 💜 💜 💜 💜<br>
                💜 💜 💜 💜 💜
            </div>
        """, unsafe_allow_html=True)
        st.success("Hearts sent your way! 💜")

# Footer
st.markdown("---")
st.markdown("""
    <p style='text-align: center; font-size: 22px; color: #9c27b0;'>
        Lots of love & pride from your big cousin ❤️
    </p>
""", unsafe_allow_html=True)

st.caption(f"Sent on {datetime.now().strftime('%B %d, %Y')}")
