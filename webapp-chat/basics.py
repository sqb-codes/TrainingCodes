# Getting started with streamlit
# 1. Open terminal/powershell
# 2. pip install streamlit
# 3. streamlit --version

import streamlit as st

st.title("My Chat App...")  # heading
st.header("Header")
st.subheader("Sub header...")
st.write("Hello User...Welcome to chat application")    # paragraph
st.markdown("**Bold text** and _italic_")

name = st.text_input("Enter your name")
age = st.slider("Select your age",1,100)
agree = st.checkbox("I agree...")

st.selectbox("Choose", ["Python", "AI", "ML"])
st.radio("Select Gender", ["Male", "Female"])
st.file_uploader("Upload Resume...")