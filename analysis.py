import streamlit as st 
import pandas as pd
from datetime import datetime
import json
import matplotlib.pyplot as plt
import seaborn as sns

def analysis():
    """
    Shows a visual summary of your mood logs.
    You can choose to see how your mood changed weekly, monthly, yearly, or overall using bar charts.
    """

    st.header("Welcome to the analysis of your mood")
    st.subheader("Here you can analysis how was your mood during weeks, years and even overall data")

    # Ask the user which type of report they want to see
    mood = st.selectbox("Which report do you want?", ['','Weekly','Monthly','Yearly', 'Overall'])

    try:
        # Read the saved mood entries from mood.json
        data = pd.read_json('mood.json')

        # Extract parts of the date to help group the mood data
        data['month'] = data['date'].dt.month     # Get the month (as a number)
        data['year'] = data['date'].dt.year       # Get the year
        data['day'] = data['date'].dt.day         # Get the day of the month

        # Convert month number to month name for better readability
        month_map = {1: 'January', 2: 'Feburary', 3: 'March', 4: 'April', 5: 'May',
                    6: 'June', 7: 'July', 8: 'August', 9: 'September',
                    10: 'October', 11: 'November', 12: 'December'
                    }
        data['month_name'] = data['month'].map(month_map)

        # Create a figure for plotting
        fig, ax = plt.subplots()

        # Get the list of unique months and years that the user has logged
        uniqueMonths = data['month_name'].unique()
        uniqueYears = data['year'].unique()

        #Weekly Mood Analysis
        if mood == 'Weekly':
            # Let user pick the month to filter weekly mood data
            selectedMonth = st.selectbox("Enter the month which you want the weekly data of", uniqueMonths)

            if selectedMonth:
                # Filter the dataset by selected month
                newData = data[data['month_name'] == selectedMonth]

                # Let the user choose the week they want to see
                week = week = st.selectbox("Pick a week to review your mood:", ["Week 1", "Week 2", "Week 3", "Week 4"])

                # Based on the selected week, filter the data further
                if week == "Week 1":
                    week_data = newData[(newData['day'] >= 1) & (newData['day'] <= 7)]
                elif week == "Week 2":
                    week_data = newData[(newData['day'] >= 8) & (newData['day'] <= 14)]
                elif week == "Week 3":
                    week_data = newData[(newData['day'] >= 15) & (newData['day'] <= 22)]
                elif week == "Week 4":
                    week_data = newData[(newData['day'] >= 23) & (newData['day'] <= 30)]
                else:
                    week_data = pd.DataFrame()  # In case something unexpected happens

            # Plot the mood frequency chart for the selected week
            sns.countplot(x='mood', hue='mood', data=week_data, ax=ax)
            ax.set_xlabel("Your different moods through out the week ")
            ax.set_ylabel("Number of times you had this mood!")
            ax.set_title(f"Mood Analysis of {week} of Month: {selectedMonth}") 
            st.pyplot(fig)               
            st.write("If the graph is empty or do not show that means you have not inputed the data of that week!")

        # Monthly Mood Analysis
        elif mood == 'Monthly':
            # Ask the user which month they want to analyze
            selectedMonth = st.selectbox("Enter the month which you want the weekly data of", uniqueMonths)
            newData = data[data['month_name'] == selectedMonth]

            if selectedMonth:
                # Create a new plot for the monthly data
                fig, ax = plt.subplots()  
                sns.countplot(x='mood', hue='mood', data=newData, ax=ax)
                ax.set_xlabel("Your different moods throughout the month")
                ax.set_ylabel("Number of times you had this mood!")
                ax.set_title(f"Mood Analysis of Month: {selectedMonth}") 
                st.pyplot(fig)

            st.write("If the other months do not show that means you have not inputed the data of that month!")

        #Yearly mood analysis
        elif mood == 'Yearly':
            # Let the user pick a year to review
            selectedYear = st.selectbox("Enter the year which you want the data of", uniqueYears)

            if selectedYear:
                # Filter the mood entries for the selected year
                yearlyData = data[data['year'] == selectedYear]

                # Create a new plot for the yearly mood breakdown
                fig, ax = plt.subplots()  
                sns.countplot(x='mood', hue='mood', data=yearlyData, ax=ax)
                ax.set_xlabel("Your different moods throughout the month")
                ax.set_ylabel("Number of times you had this mood!")
                ax.set_title(f"Mood Analysis of Year: {selectedYear}") 
                st.pyplot(fig)

            st.write("If the other years do not show that means you have not inputed the data of that year!")               

    except FileNotFoundError:
        # Show a friendly message if the data file doesn’t exist
        st.write("We cannot find any file")
