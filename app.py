#stream lit
import streamlit as st

st.set_page_config(page_title = "growth mindset challenge" )
st.title("Growth mind set challenge: web app with streamlit ")

st.header("wellcome to your groeth journey")
st.write("Embrance challenge, learn from mistake, and unlock your full potential This AI-powered app help you build a Growth a mindset with reflections challenges and achievment")

st.header("Todays growth mindset quote")
st.write("sucess is not final,fialure is not fatal: it is the courage to continue that count.-winston churchill")

st.header("What your's challenge today?")
user_input = st.text_input("Describe a challenge you are facing:")

if user_input:
    st.success(f"you are facing: {user_input}. keep pushing forward towards your goal!")
else:
    st.warning("Tell us about your challenge to get started!")

st.header("Reflect on your learning") 
reflection = st.text_area("write your reflection here:")

if reflection:
    st.success(f"Great insight your reflection:{reflection}")
else:
    st.info("Reflicting on past experience help you grow! share your difficulties")

st.header("Celebrate your wins!")
achievment = st.text_input("share something yo've recently accomplished:")

if achievment:
    st.success(f"Amazing you achieved!{achievment}")
else:
    st.info("big or small , every achievments counts! share one now")

st.write("- - -")
st.write("Keep believing your self. Growth is a journey, not a destination!")
st.write("**Created By Rahib Siddiqui**")
