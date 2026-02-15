import streamlit as st
from chat_logic import main

st.set_page_config("Chatbot")
st.title("Instant Chatbot")
st.write("Chatbot for news, weather, cricket, stock...")

user_input = st.text_input("Enter your message")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if st.button("Ask"):    # button click
    if user_input.strip() != "":    # check if text box is not empty
        st.session_state.chat_history.append(("You", user_input)) # storing in session what user input is
        response = main(user_input)
        st.session_state.chat_history.append(("Bot", response))

for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")