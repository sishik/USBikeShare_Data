import time
import pandas as pd
import numpy as np
import sys

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
     print('Hello! Let\'s explore some US bikeshare data!')
     """
     Asks user to specify a city, month, and day to analyze.

     Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
     """
     # get user input for city (chicago, new york city, washington).
     while True:
        city = input("\nEnter one of the city among \"CHICAGO\" , \"NEW YORK \" , \"WASHINGTON\" to explore the bikeshare data\n").lower()
        if city not in ('chicago', 'new york', 'washington'):
            print("\n   Not a valid city. Please enter the correct city OR would you like to exit.  \n")
            x=input('\n enter "no" to exit and "yes" to continue.\n').lower()
            if x != 'yes':
                exit()
                
        else:
            break
     # get user input for month (all, january, february, ... , june) 
     while True:
        month = input("\nEnter name of the month \n January \n February \n March \n April \n May \n June  to filter by, or \"all\" to apply no month filter\n").lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Not a valid month. please choose the month from given list only.\n")
        else:
            break
            
     #  get user input for day of week (all, monday, tuesday, ... sunday)
     while True:
        day = input("\nEnter the name of the day of week  \n Sunday \n Monday \n Tuesday \n  Wednesday \n Thursday \n Friday \n Saturday \nto filter by, or \"all\" to apply no day filter\n").lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print("Not a valid day. please enter the day correctly.\n")
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
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    else:
        df['month']

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    else:
        df['day_of_week'] 


    return df


def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""
     
    print('\n\n\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    popular_month = df['month'].mode()[0]
    if popular_month == 1:
        print('Most common month is: ',popular_month,' i.e January \n')
    elif popular_month == 2:
        print('Most common month is: ',popular_month,' i.e February\n')
    elif popular_month == 3:
        print('Most common month is: ',popular_month,' i.e March \n') 
    elif popular_month == 4:
        print('Most common month is: ',popular_month,' i.e April \n')
    elif popular_month == 5:
        print('Most common month is: ',popular_month,' i.e May \n')
    elif popular_month == 6:
        print('Most common month is: ',popular_month,' i.e June \n')
    else:
        print('\n')

    # display the most common day of week
    popular_week = df['day_of_week'].mode()[0]
    print('Most common week is: ',popular_week,'\n')

    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour,'\n')

    print("This took %s seconds." % (time.time() - start_time),'\n')
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n\n\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    print('printing the most commonly used start station...\n')
    common_Start_Station = df['Start Station'].mode()[0]
    print(' most common start station : ' ,common_Start_Station,'\n')

    #  display most commonly used end station
    print('printing most commonly used end station..\n')
    common_End_Station = df['End Station'].mode()[0]
    print('most common End station : ' ,common_End_Station,'\n')

    # display most frequent combination of start station and end station trip
    print('displaying most frequent combination of start station and end station trip....\n')
    df['most_common_trip'] = df['Start Station'].str.cat(df['End Station'], sep = 'to')
    common_trip = df['most_common_trip'].mode()[0]
    print ('Most common trip from start to end:', common_trip,'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n\n\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('dispalying total travel time... \n')
    total_hours_travel = df['Trip Duration'].sum()
    time1 = total_hours_travel 
    hour1 = time1 // 3600
    time1 %= 3600
    minutes1 = time1 // 60
    time1 %= 60
    seconds1 = time1
    print("{}h:{}m:{}s".format(hour1, minutes1, seconds1),'\n\n')

    # TO DO: display mean travel time
    print('displaying the mean travel time.....\n')
    avg_travel = df['Trip Duration'].mean()
    time2 = avg_travel
    minutes2 = time2 // 60
    time2 %= 60
    seconds2 = time2
    print ('Average travel time (mins) {}m:{}s:'.format(minutes2,seconds2),'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """try block is used to except key error'
       As washington.csv file doesn't have data regarding 'User_type' & 'Gender'.
       So, If we try to print its data then KeyError might occur
    """
    try:
        
        """Displays statistics on bikeshare users."""
        print('\n\n\nCalculating User Stats...\n')
        start_time = time.time()
        # Display counts of user types
        user_type = df.groupby(['User Type']).size().reset_index().rename(columns={0:'count'})
        print ('\n',user_type)
        #  Display counts of gender
        gender_count=df.groupby(['Gender']).size().rename(columns={0:'Gender_Count'})
        print('\n',gender_count)
        # Display earliest, most recent, and most common year of birth
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        print ('Year of birth - Earliest: {}, most recent: {}, most common: {}'.format(earliest, most_recent, common),'\n')
    except KeyError:
        print('data regarding gender and year of birth of the user for washington is not available.\n')

        print("This took %s seconds." % (time.time() - start_time))
        print('-'*40)

def individual_trip_display(df):
    """Displays individual trip data if asked by users."""
    while True:
          individual_data = input('\n \nWould you like to explore individual data? Enter yes or no.\n').lower()
          if individual_data != 'yes':
              break
          print('printing individual trip data.\n')
          number_of_head = int(input('enter the number of data you want to explore.\n For e.g. 5,10,15..\n'))
          #increases the column width by 500 so that long string can be displayed for individual data.
          pd.set_option('max_colwidth', 500)
          print(df.head(number_of_head).reset_index())
          """After printing first N data enetered by user.
          Here it will again ask the user, If they want explore more data then user should press yes.
          """     
          option=input("Do you want to explore more individual trip data?\n Enter yes or no.\n")
          if option != 'yes':
                break
          new_number_of_head = int(input('enter the number of data you want to explore more.\n For e.g. 5,10,15..\n'))
          print(df.head(number_of_head+new_number_of_head).reset_index())
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        individual_trip_display(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
           
        


if __name__ == "__main__":
    main()
