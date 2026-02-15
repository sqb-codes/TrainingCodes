import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page Config
st.set_page_config(
    page_title="Smart Student Dashboard",
    page_icon="",
    layout="wide"
)


if "students" not in st.session_state:
    st.session_state.students = pd.DataFrame({
        "Name": ["John", "Max", "Smith"],
        "Math": [78,99,45],
        "Science": [87,77,67],
        "English": [60,73,87]
    })


# Sidebar
st.sidebar.title("Dashboard Settings")

selected_page = st.sidebar.radio(
    "Navigate",
    ["Home", "Add Student", "Analytics", "Upload Data", "AI Assistant"]
)

theme_color = st.sidebar.color_picker("Pick Theme Accent","#454542")


# Home Page
if selected_page == "Home":
    st.title("Smart Student Dashboard")
    st.success("Welcome to your interactive dashboard!!!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Students",len(st.session_state.students))

    with col2:
        avg_score = st.session_state.students[["Math","Science","English"]].mean().mean()
        st.metric("Average Score:", round(avg_score, 2))

    with col3:
        top_student = st.session_state.students["Name"][
            st.session_state.students[["Math","Science","English"]].mean(axis=1).idxmax()
        ]
        st.metric("Top Student",top_student)

    st.subheader("Student Records")
    st.dataframe(st.session_state.students)

elif selected_page == "Add Student":
    st.title("Add Student - Smart Student Dashboard")
    st.success("Add new student...")

elif selected_page == "Analytics":
    st.title("Student Analytics - Smart Student Dashboard")

elif selected_page == "Upload Data":
    st.title("Upload Student Data - Smart Student Dashboard")
    st.success("Upload students through CSV files...")

elif selected_page == "AI Assistant":
    st.title("AI Assistant - Smart Student Dashboard")
    st.success("Ask AI anything...")