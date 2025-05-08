import streamlit as st
import pandas as pd 
import json
import datetime 
from detector import mood_data
from analysis import analysis

# This is the main entry point of the app where navigation is handled

# Sidebar menu to let users move between different parts of the app
page = st.sidebar.selectbox(
    "Navigate to:",
    ("🏠 Home", "📝 Log Mood", "📊 Analysis Report")
)

# Sidebar details and intro message
st.sidebar.title("Thank you for using the Mood & Habit Tracker!")
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)

# Short description about the purpose of the app
st.sidebar.text("This app is the part of the project of CS 196 II. This app has been made by Sujal Adhikari. This app helps you enter your mood, store your mood on the basis of date, and then get the weekly, monthly and yearly report of how your days has been like.")
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.markdown("<br>", unsafe_allow_html=True)

# Author and course details
st.sidebar.text("Made by: Sujal Adhikari")
st.sidebar.text("Caldwell ID: 455841")
st.sidebar.text("CS 196 II")
st.sidebar.text("Professor: Dr Vlad Veklser")

# If the user selects Home, show the welcome screen
if page == '🏠 Home':
    st.title(" Welcome to Your Mood & Habit Tracker")
    st.subheader("Track your habits. Understand your moods. Improve your day — one reflection at a time.")
    st.subheader("🧠 Build self-awareness through daily check-ins and visual insights.")
    st.subheader("🔐 Your data stays local and private — no accounts, no tracking.")
    st.text("To get started please select the 📝 Log Mood to input the data")

# If the user selects Log Mood, call the mood_data() function to input a new entry
elif page == '📝 Log Mood':
    mood_data()

# If the user selects Analysis Report, call the analysis() function to show mood insights
elif page == '📊 Analysis Report':
    analysis()
