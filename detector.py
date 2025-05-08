import streamlit as st 
import pandas as pd
from datetime import datetime
import json

def mood_data():
    """
    This function allows the user to log their mood for a specific day.
    The user selects a mood, rates its intensity, writes a short explanation,
    and picks a date. The information is saved to a JSON file for later analysis.
    """

    st.subheader("Can you please fill out the details !")

    # Let the user choose how they’re feeling using a set of emojis + mood labels
    moodToday = st.selectbox("Can you enter your mood !", [
        "😊 Happy",
        "😔 Sad",
        "😡 Angry",
        "😐 Neutral",
        "😨 Anxious",
        "😴 Tired",
        "😍 Loved",
        "😤 Frustrated",
        "🤩 Excited",
        "😕 Confused"
    ])

    # Remove the emoji and keep only the mood label
    realMood = str(moodToday)
    realMood = realMood[1:]

    # Ask the user how strongly they feel this mood using a slider
    range = st.slider(f"Can you please explain how {realMood} are you feeling today")

    # Let the user describe why they feel that way
    text = st.text_area(f"Can you explain why are you feeling {realMood} today?")

    # Ask for the date when the user experienced this mood
    date = st.date_input(f"Can you enter the date you felt {realMood} ")
    realDate = date.isoformat()

    # When the submit button is clicked, begin saving the data
    if st.button("Submit"):
        if realMood: 
            st.success("Mood login successful !")
        else:
            st.warning("You cannot leave this field empty!")

        # Create a dictionary to store the mood entry
        data = {
            "mood": realMood,
            "range": range, 
            "text": text, 
            "date": realDate
        }

        # Try loading existing mood entries from mood.json
        try:
            with open("mood.json", 'r') as file:
                storingData = json.load(file)
                if not isinstance(storingData, list):
                    storingData = []
        except (FileNotFoundError, json.JSONDecodeError):
            # If the file doesn’t exist or is corrupted, start fresh
            storingData = []

        # Add the new entry to the list
        storingData.append(data)

        # Save the updated list back to the JSON file
        with open("mood.json", 'w') as file:
            json.dump(storingData, file, indent=2)
