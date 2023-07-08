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
    


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = str(input("Would you like to review data for Chicago, New York City, or Washington?\n")).lower()
    while city not in CITY_DATA:
        print("\nOops! It looks like you have entered an incorrect city.\n")
        city = str(input("Please enter one of the options to review data:\nChicago \nNew York City \nWashington?\n")).lower()
    print("\nYou have selected to review data for {}!".format(city.title()))



    # TO DO: get user input for month (all, january, february, ... , june)
    month = str(input("Please enter which month's data to review - January, February, March, April, May, June, or All?\n")).title()
    while month not in ('January', 'February', 'March', 'April', 'May', 'June', 'All'):
        print("\nOops! It seems your entry is invalid. Please try again.")
        month = str(input("\nPlease enter which month's data to review - January, February, March, April, May, June, or All?\n")).title()



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = str(input("\nGreat! Now please enter which days' data in {} you want to review - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All?\n".format(month.title()))).title()
    while day not in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'All'):
        print("\nOops! It seems your entry is invalid. Please try again.")
        day = str(input("Enter which days' data in {} you want to review - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All?\n".format(month.title())))

    print("\nYou have selected to review data for: {} / {} / {}.\n".format(city.title(),month,day))

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
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'All':
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    

    print("\nTravel Stats:\nThe most common month of travel was: {}; \nThe most common weekday of travel was: {}; \nWhile the most common start hour of travel was: {}.00 HRS!".format(common_month, common_day, common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    popular_route = df['Start Station'].str.cat(df['End Station'], sep = ' ===> ').mode()[0]

    print("\nStation Stats:\nThe most common start station was: {}; \nThe most common end station was: {}; \nWhile the most frequent combination of start station and end station was: {}!".format(common_start_station, common_end_station, popular_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print("The total travel time was: {} days; and the mean travel time was: {} minutes!".format((total_travel_time/86400), (mean_travel_time/60)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    try:
        gender_cat = df['Gender'].value_counts()
        print("\nGender Category:\n{}".format(gender_cat))
    except:
        print("\nGender Category:\nNo gender data available for this selection.")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(df['Birth Year'].min())
        latest_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])

        print("\nBirth Data:\nThe earliest birth year was: {}; \nThe most recent birth year was: {}; \nWhile the most common birth year was: {}!".format(earliest_birth_year, latest_birth_year, common_birth_year))

    except:
        print("\nBirth Year:\nNo birth data available for this selection.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(city):
    
    """Displayed upon request by the user
    Prompt the user if they want to see 5 lines of raw data
    Display 5 records from the selected city if 'yes' is selected
    Iterate prompts and display the next 5 lines of raw data at each iteration
    Stop the program when the user selects 'no' or there is no more raw data to display.

    Args:
        (df): the data frame of the selected city.
    Returns:
        (df.(head)) - five rows of raw data for all columns
    """
    df = pd.read_csv(CITY_DATA[city])

    answers = ['YES','NO']
    i = 0
    
    user_input = str(input("\nWould you like to view the raw data records?\nPlease type 'YES' or 'NO'\n\n")).upper()

    #confirm whether or not the user wants to view the raw data
    while True:
        while user_input not in answers:
            user_input = str(input("\nWould you like to view the raw data records?\nPlease type 'YES' or 'NO'.\n\n")).upper()


        #displaying batch of 5 raw data records if user types 'YES' using the df.head() method
        if user_input == 'NO':
            break
        elif user_input == 'YES':
            print(df.head())


            #to confirm whether or not the user wants additional data to be displayed 
            while True:
                user_input = str(input("\nWould you like see more raw data records?\nPlease type 'YES' or 'NO'\n\n")).upper()
                if user_input == 'NO':
                    break
                elif user_input == 'YES':
                    i += 5
                    print(df[i:i+5])


    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

    raw_data(city)


if __name__ == "__main__":
	main()
