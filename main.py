import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Happy 16th Birthday | Urooj Fatima",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Clean & Elegant Styling
st.markdown("""
    <style>
    .main-title {
        font-size: 52px;
        font-weight: 700;
        color: #2C3E50;
        text-align: center;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 28px;
        color: #34495E;
        text-align: center;
        font-weight: 500;
    }
    .message {
        font-size: 24px;
        line-height: 1.8;
        color: #2C3E50;
        text-align: center;
        max-width: 700px;
        margin: 30px auto;
    }
    .highlight {
        color: #E91E63;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-title">Happy 16th Birthday</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Urooj Fatima</p>', unsafe_allow_html=True)

# Main Message
st.markdown("""
    <p class="message">
        Dear Urooj,<br><br>
        
        Happy 16th Birthday! 🎉<br><br>
        
        Watching you grow into a confident, intelligent, and wonderful young woman has been really special. 
        As your cousin, I’ve always seen you like a little sister, and I’m truly proud of the person you are becoming.<br><br>
        
        May this new chapter of your life bring you clarity, success, beautiful experiences, and all the happiness you deserve. 
        Keep shining, keep learning, and continue being your amazing self.<br><br>
        
        I’m always here for you — whenever you need advice, a chat, or just someone in your corner.<br><br>
        
        Wishing you an unforgettable Sweet 16!
    </p>
""", unsafe_allow_html=True)

# Interactive Section
st.markdown("### 🎈 Celebrate with a Wish")
col1, col2 = st.columns(2)

with col1:
    if st.button("🎂 Make a Birthday Wish", use_container_width=True):
        st.balloons()
        st.success("Wish sent into the universe ✨")

with col2:
    if st.button("🌟 Send Good Vibes", use_container_width=True):
        st.snow()
        st.success("Positive energy delivered 💫")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #666; font-size: 18px;'>"
    "Made with love and pride by your big cousin ❤️</p>", 
    unsafe_allow_html=True
)
st.caption(f"Sent on {datetime.now().strftime('%B %d, %Y')}")
