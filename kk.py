import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

df = pd.read_csv(CITY_DATA['washington'])
# print(df.head())
df['Start Time'] = pd.to_datetime(df['Start Time'])
# extract month and day of week from Start Time to create new columns
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.day_name()
df['hour'] = df['Start Time'].dt.hour

def display_raw_data(df):
    """
    Display raw data from a Pandas DataFrame in chunks of 5 lines upon user request.

    Args:
        df (pd.DataFrame): The DataFrame containing the raw data.
    """
    index = 0

    while True:
        # Prompt the user if they want to see 5 lines of raw data
        user_input = input("Do you want to see 5 lines of raw data? Enter 'yes' or 'no': ").lower()

        if user_input == 'yes':
            # Display the next 5 lines of raw data
            print(df.iloc[index:index + 5])
            index += 5
        else:
            break

# Call the function to display raw data
display_raw_data(df)
