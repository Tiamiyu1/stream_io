import streamlit as st
import pandas as pd
import numpy as np
import time

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

# Function to load and process data based on user input
@st.cache_data  # Cache the function's output
def load_and_process_data(city, month, day):
    # Load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city.lower()],  index_col=False).drop(columns=['Unnamed: 0'])

    # Convert 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    # df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filter by month if applicable
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        df = df[df['month'] == month]
        # df = df[df['month'] == months.index(month) + 1]

    # Filter by day of week if applicable
    if day != 'All':
        df = df[df['day_of_week'] == day]

    return df

# Streamlit App
def main():
    st.title("US Bikeshare Data Exploration Tiamiyu")
    st.write("Explore bikeshare data for different cities.")

    # User input: City, Month, and Day
    st.sidebar.subheader("US Cities")
    city = ("Chicago", "New York City", "Washington")
    city = st.sidebar.radio(label= "Select a city to explore", options= city)
    # city = st.selectbox("Select a City:", ["Chicago", "New York City", "Washington"])
    month = st.selectbox("Select a Month:", ["All"] + ['January', 'February', 'March', 'April', 'May', 'June'])
    day = st.selectbox("Select a Day:", ["All"] + ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

    # Button to trigger analysis
    analyze_button = st.button("Explore!")
    
    if analyze_button:
        # Load and process data when the "Analyze" button is clicked
        df = load_and_process_data(city, month, day)

        # Display analysis results
        st.subheader("Calculating The Most Frequent Times of Travel...")
        st.write("Most Common Month: ", df['month'].mode()[0])
        st.write("Most Common Day of the Week: ", df['day_of_week'].mode()[0])
        st.write("Most Common Start Hour:", str(df['hour'].mode()[0]) + ':00 HR')

        st.subheader("Calculating The Most Popular Stations and Trip...")
        st.write("Most Common Start Station: ", df['Start Station'].mode()[0])
        st.write("Most Common End Station: ", df['End Station'].mode()[0])
        st.write("Most Frequent Combination of Start and End Stations: ", df.groupby(['Start Station', 'End Station']).size().idxmax())

        st.subheader("Calculating Trip Duration...")
        st.write("Total Travel Time: ", np.sum(df['Trip Duration']), 'Secs')
        st.write("Average Travel Time: ", round(np.mean(df['Trip Duration']), 3), 'Secs')

        st.subheader("Calculating User Stats...")
        st.write("Count of User Type: ", df['User Type'].value_counts())
        
        if 'Gender' in df.columns.tolist():
            st.write("Count of Gender: \n", df['Gender'].value_counts())
            st.write("The earliest, most recent and most common years of birth are {}, {} and {} respectively."
            .format(int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(df['Birth Year'].mode()[0])))

        # Option to view raw data
        st.subheader("Raw Data:")
        st.write(df.head())

if __name__ == "__main__":
    main()
