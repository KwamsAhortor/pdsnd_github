# Exploring US Bikeshare Data
This is a project to develop a python script that queries a user database to uncover bike share usage patterns for a bike share system provider in the United States. The project seek to compare the system usage between three large cities: Chicago, New York City, and Washington, DC.

## Date created
08/09/2021

## Project Title
Bikeshare Data Analysis for Q1 and Q2 2017

## Description
This project is to write a script that provides statistics and analytics information for the first and second quarter of 2017 for bicycle ride sharing company in the US.

The location scope for the project included Washington, New York city and Chicago. The time scope spans 01/01/2021 to 31/06/2021 and includes about 1,000,000 individual bike rides.

The script solicits user input to return query results.


### The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two additional columns:
- Gender
- Birth Year

### Statistics Computed
Popular times of travel
- most common month
- most common day of week
- most common hour of day

Popular stations and trip
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

Trip duration
- total travel time
- average travel time

User info
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

Graphs
Bar graphs of the frequency of the following demographics are available from input prompt.
- Start Station
- End Station
- User Type
- Gender
- Birth Year


## Files used
1. washington.csv
2. new_york_city.csv
3. chicago.csv

### Credits
The data used for the project was provided by [Motivate](https://www.motivateco.com).

The data was prepared, wrangled and cleaned by [Udacity](https://www.udacity.com).

