import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?: ").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Invalid input. Please enter one of the specified cities.")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month? January, February, March, April, May or June? - Type 'all' to selcet all months: ").lower()
        if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            print("Invalid input. Please enter one of the specified months.")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        # day = input("Which day? Please type your response as an integer from 1 to 7 (e.g., 1=Sunday): ")
        day = input("Which day? Monday, Tueday, Wednesday, Thursday, Friday, Saturday or Sunday? - Type 'all' to selcet all days: ")
        # if day not in['1','2','3','4','5','6','7']:
        if day not in['monday','tuesday','wednesday','thursday','friday','saturday','sunday', 'all']:
            print("Invalid input. Please enter one of the specified days.")
            continue
        else:
            break
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df.month==month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df.day_of_week==day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most Common Month:', df['month'].mode()[0])

    # display the most common day of week
    print('Most Common Day of the Week:', df['day_of_week'].mode()[0])

    # display the most common start hour
    print('Most Common Start Hour:', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most Common Start Station:", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("Most Common End Station:", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip

    print("Most Common End Station:", df['Start Station'].mode()[0], "***and***",  df['End Station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total Time Travel: ", np.sum(df['Trip Duration']), 'Secs')


    # display mean travel time
    print("Average Time Travel: ", round(np.mean(df['Trip Duration']), 3), 'Secs')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Count of User Type: ",'\n',df['User Type'].value_counts())

    # Display counts of gender
    if 'Gender' in df.columns.tolist():
        print("Count of Gender: ",'\n',df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
        print("The earliest, most recent and most common years of birth are {}, {} and {} respectively."
            .format(int(df['Birth Year'].min()), int(df['Birth Year'].max()), int(df['Birth Year'].mode()[0])))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """
    Display raw data from a Pandas DataFrame in chunks of 5 lines upon user request.

    Args:
        df (pd.DataFrame): The DataFrame containing the raw data.
    """
    index = 0

    while True:
        # Prompt the user if they want to see 5 lines of raw data
        user_input = input("Do you want to see 5 lines of the raw data? Enter 'yes' or 'no': ").lower()

        if user_input == 'yes':
            # Display the next 5 lines of raw data
            print(df.iloc[index:index + 5])
            index += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart the Data Exploration? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
