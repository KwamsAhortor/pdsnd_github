import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        
        while statement is used to reject or approve input.
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city do you want to explore').lower()
    while city not in list(CITY_DATA.keys()):
            print("Oops! It seems your input is incorrect. Please try again or input 'ls' to see list of cities")
            city = input('Which city do you want to explore').lower()
            if city == 'ls':
                print('Select one of these: {}'.format(list(CITY_DATA.keys())))


    # get user input for month (all, january, february, ... , june)
    month = input("Which month do you want to explore. Select 'all' for no filter").lower()
    while month not in months:
        if month == 'all':
            break
        else:
            print("Oops! It seems your input is incorrect. Please try again or input 'ls' to see list of months")
            month = input('Which month do you want to explore').lower()
            if month == 'ls':
                print('Select one of these: {}'.format(months))


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day do you want to explore. Select 'all' for no filter").lower()
    while day not in days:
        if day == 'all':
            break
        else:
            print("Oops! It seems your input is incorrect. Please try again or input 'ls' to see list of months")
            day = input('Which day do you want to explore').lower()
            if day == 'ls':
                print('Select one of these: {}'.format(days))
    

    print('-'*80)
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
    d_parser = lambda x: pd.to_datetime(x) #creating a date_parser function.
    df = pd.read_csv(CITY_DATA[city], parse_dates=['Start Time', 'End Time'], date_parser=d_parser)

    # convert the Start Time column to datetime. (No need to because dates are already parsed)
    #df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day Of Week'] = df['Start Time'].dt.day_of_week

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Month'] == month]
    elif month == 'all':
        df

    # filter by day of week if applicable
    if day != 'all':
        day = days.index(day) + 1
        # filter by day of week to create the new dataframe
        df = df[df['Day Of Week'] == day]
    elif month == 'all':
        df
    return df


def time_stats(df, month, day):
    """
    Displays statistics on the most frequent times of travel.
    Args:
        (pd.DataFrame) df -- returns the filtered pandas dataframe
        (str) city -- name of the city to analyze
        (str) month -- name of the month
        (str) day -- name of the day of week

    Variables:
        (float) start_time -- returns the 'time.time()' function starts running. Used calculate duration of code run.
        (str) most_frequented_month -- return the month that received the most travels. 
            if condition is applied to prevent filters that are month-specific from running a ValueError.
        (str) most_frequented_day -- return the day that received the most travels.
            if condition is applied to prevent filters that are day-0specific from running a ValueError.
        (str) most_frequented_hour -- return the hour of the day that received the most travels
    """
    print('\n***Calculating The Most Frequent Times of Travel***\n')
    start_time = time.time()

    # display the most common month
    if month == 'all':
        frequented_month = df['Month'].value_counts().idxmax()
        most_frequented_month = months[frequented_month - 1].title()
        print('Most_frequented_month: {}'.format(most_frequented_month))

    # display the most common day of week
    if day == 'all':
        frequented_day = df['Day Of Week'].value_counts().idxmax()
        most_frequented_day = days[frequented_day].title()
        print('Most_frequented_day: {}'.format(most_frequented_day))

    # display the most common start hour
    most_frequented_hour = (df['Start Time'].dt.hour).value_counts().idxmax()
    print('Most_frequented_hour: {}'.format(most_frequented_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    Args:
        (pd.DataFrame) df -- returns the filtered pandas dataframe

    Variables:
        (float) start_time -- returns the 'time.time()' function starts running. Used calculate duration of code run.
        (str) most_frequent_start_station -- return the most commonly used start station
        (str) most_frequent_end_station -- return the most commonly used end station
        (str) most_frequent_start_end_station -- return a combination of start and end station (seperated by
            '||') that is most commonly used.
    """
    print('\n***Calculating The Most Popular Stations and Trip***\n')
    start_time = time.time()

    # display most commonly used start station
    most_frequent_start_station = df['Start Station'].value_counts().idxmax()
    print('Most frequent start station: {}'.format(most_frequent_start_station))

    # display most commonly used end station
    most_frequent_end_station = df['End Station'].value_counts().idxmax()
    print('Most frequent end station: {}'.format(most_frequent_end_station))

    # display most frequent combination of start station and end station trip
    most_frequent_start_end_station = pd.concat([df['Start Station'], df['End Station']], axis = 1).value_counts().idxmax()
    print('Most frequent start/end station combination: {} || {}'.format(most_frequent_start_end_station[0], most_frequent_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.
    Args:
        (pd.DataFrame) df -- returns the filtered pandas dataframe

    Variables:
        (float) start_time -- returns the 'time.time()' function starts running. Used calculate duration of code run.
        (float) total_duration -- return the total duration of all trips in hours.
        (float) mean_duration -- return the average duration per each trip in minutes.
    """
    print('\n***Calculating Trip Duration***\n')
    start_time = time.time()

    # display total travel time
    total_duration = round(df['Trip Duration'].sum()/3600, 2)
    print('Total trip duration: {}hrs'.format(total_duration))

    # display mean travel time
    mean_duration = round(df['Trip Duration'].mean()/60, 2)
    print('Average trip duration: {}mins'.format(mean_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def user_stats(df):
    """Displays statistics on bikeshare users.
    Args:
        (pd.DataFrame) df -- returns the filtered pandas dataframe

    Variables:
        (float) start_time -- returns the 'time.time()' function starts running. Used calculate duration of code run.
        (pd.series) user_type_count -- return the count of the user types in df
            if statement is applied to exclude df with no 'Gender' column.
        (pd.series) gender_count -- return the aggregate sum of the gender of users including NaN values.
            if statement is applied to exclude df with no 'Gender' column.
        (int) earliest_year -- return the year which is earliest
            if statement is applied to exclude df with no 'Gender' column.
        (int) recent_year -- return the year which is the most recent.
            if statement is applied to exclude df with no 'Gender' column.
        (int) most_common_year -- return the most frequent year.
           if statement is applied to exclude df with no 'Gender' column. 
    """
    print('\n***Calculating User Stats***\n')
    start_time = time.time()

    # Display counts of user types
    if 'Gender' in df.columns:
        user_type_count = df['User Type'].value_counts()
        print('Total users by user type category:\n{}'.format(user_type_count))

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts(dropna=False)
        print('\nTotal users by gender:\n{}\n'.format(gender_count))

    # Display earliest, most recent, and most common year of birth
    if 'Gender' in df.columns:
        earliest_year = round(df['Birth Year'].min())
        recent_year = round(df['Birth Year'].max())
        most_common_year = round(df['Birth Year'].value_counts().idxmax())
        print('Birth years:\nEarliest year: {}\nRecent year: {}\nMost common year: {}\n'.format(earliest_year, recent_year, most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def category_count_graph(df):
    """Displays statistics on bikeshare users.
    Args:
        (pd.DataFrame) df -- returns the filtered pandas dataframe
    
    Variables:
        (list) categories -- return selected list of columns in df to used in graph.
        (str) category -- return input for choise of category to view in graph

        while statement is used to reject or approve input.    
    """
    print('\n***View Graphs Based on Categories***\n')
    start_time = time.time()

    view_graph = input('Would you like to view some charts of some of the demographics? Enter yes or no?').lower()
    while view_graph == 'yes':
        categories = list(df.columns[-5:])
        category = input('Select one of these categories\n{}'.format(categories)).title()
        while category not in categories:
            print('Oops! It seems your input is incorrect. Please try again.\nSelect one of these {}'.format(categories))
            category = input('Select one of these categories\n{}'.format(categories)).title()
        pd.DataFrame(df[category].value_counts()).plot(kind='bar')
        plt.title('Count of {}'.format(category))
        plt.xlabel('category')
        plt.ylabel('Count')
        plt.show()
        view_graph = input('Would you like to view more charts? Enter yes or no?').lower()
        if view_graph == 'no':
            break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def display_data(df):
    """ Displays a preview of the data (df) in increment of 5 rows upon each request
    Args:
        (pd.DataFrame) df -- returns the filtered pandas dataframe 
    
    Variables:
        (float) start_time -- returns the 'time.time()' function starts running. Used calculate duration of code run.
        (str) view_data -- input 'yes' to return 5 rows of data (df), 'no' to break the loop and end the function.

        while statement is used to reject or approve input.

    """
    print('\n***View Individual Trip Data***\n')
    start_time = time.time()

    view_data = input('Would you like to view 5 rows of individual trip data? Enter yes or no?').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input('Would you like to view 5 more rows? Enter yes or no').lower()
        if view_data == 'no':
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print('FILTERS\n City: {}    Month: {}    Day: {}'.format(city, month, day))
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        category_count_graph(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    return df

if __name__ == "__main__":
	main()

