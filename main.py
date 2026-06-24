import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Happy 16th Birthday Sis! 🎀", page_icon="🌸", layout="centered")

# Cute pink theme
st.markdown("""
    <style>
    .big-font { 
        font-size: 65px !important; 
        font-weight: bold; 
        color: #FF69B4; 
        text-align: center;
        text-shadow: 3px 3px 6px #FFB6C1;
    }
    .message { 
        font-size: 29px; 
        text-align: center; 
        color: #4B0082; 
        line-height: 1.6;
    }
    .heart { color: #FF1493; font-size: 40px; }
    </style>
""", unsafe_allow_html=True)

st.title("🎀 HAPPY 16TH BIRTHDAY MY SWEET COUSIN! 🌷")

st.markdown('<p class="big-font">Happy Sweet 16! 🎉</p>', unsafe_allow_html=True)

name = st.text_input("Her name (optional)", value="Princess")

st.markdown(f"""
    <p class="message">
        To my adorable little sister {name} 💖<br><br>
        
        Happy 16th Birthday!! 🎂✨<br>
        You’ve grown into such a beautiful, kind, and amazing girl. 
        Watching you grow up has been one of the best parts of my life. 
        Keep shining bright, chasing your dreams, and never forget how special you are.<br><br>
        
        I’m always here for you — through cake, drama, laughs, and everything in between ❤️<br><br>
        
        Have the most magical day ever filled with love, presents, and all your favorite things!
    </p>
""", unsafe_allow_html=True)

# Cute interactive buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🌸 Send a big hug"):
        st.success("Hug delivered with extra love! 🤗")
with col2:
    if st.button("🍭 Sweet 16 wishes"):
        st.balloons()
        st.success("Wishes sent! Make a wish on the candles ✨")
with col3:
    if st.button("💖 Heart explosion"):
        st.success("💖💖💖💖💖")

st.snow()
st.balloons()

st.markdown("---")
st.markdown("**Made with tons of love by your big cousin** ❤️")
st.caption(f"Sent on {datetime.now().strftime('%B %d, %Y')} | You're officially 16! 🎂")
