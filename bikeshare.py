import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#defines the filters by name of the city , month and day
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
    # i use .lower() method to lowercase the word that user enter because its define in lowercase
    #take the input from user
    city = input("Please choose the name of the city you want from the following three cities (chicago, new york city, washington) : ").lower() 
    #if user enter invalid inPut
    while city not in CITY_DATA.keys() :  
        print("Invalid input, Please choose a correct city from the three available cities")
        #take input again
        city = input("Please choose the correct name of the city you want from the following three cities (chicago, new york city, washington) : ").lower() 
    
    # TO DO: get user input for month (all, january, february, ... , june)
    # create a list of monthes and add (all) option to choose all monthes together Without filtering 
    monthes = ['january','february','march','april','may','june','all']
    #get the input from user
    month = input("Please choose one of the months from the following (january,february,march,april,may,june,all) : ").lower()
    #if user enter invalid inPut
    while month not in monthes :  
        print("Invalid input, Please choose a correct month from the available monthes")
        #take input again
        month = input("Please choose one of the months from the following (january,february,march,april,may,june,all) : ").lower() 
        


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    # create a list of days and add (all) option to choose all days together Without filtering
    days = ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']    
    #get the input from user
    day = input("Please choose one of the days from the following (saturday,sunday,monday,tuesday,wednesday,thursday,friday,all) : ").lower()
    #if user enter invalid inPut
    while day not in days : 
        print("Invalid input, Please choose a correct day from the available days")
        #take input again
        day = input("Please choose one of the days from the following (saturday,sunday,monday,tuesday,wednesday,thursday,friday,all) : ").lower() 

    print('-'*40)
    return city, month, day

#to get the data with the city name and filtered by month and day
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
    #read data from CITY_DATA Dictionary into dataframe
    df = pd.read_csv(CITY_DATA[city])
    #new datafram to convert Start Time Column from string to datetime using pandas
    df['Start Time'] = pd.to_datetime(df['Start Time']) 
    #get the month and weekday from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.weekday_name
    
    #filters by month and day if applicable:
    if month != 'all' :
        #get the index of list (have a zero index) to get value in intger 
        months = ['january','february','march','april','may','june']
        month = months.index(month) + 1
        #new dataframe filters by month
        df = df[df['month'] == month]
        #new dataframe filters by day
    if day != 'all' : 
        df = df[df['week_day'] == day.title()]
    
    return df

#take the output(dataframe) of previous and it's been the input of this function (df)
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    #mode gives us the most common value 
    # TO DO: display the most common month
    comm_month = df['month'].mode()[0]
    print("The Most Common Month Is : " + str(comm_month))

    # TO DO: display the most common day of week
    comm_day = df['week_day'].mode()[0]
    print("The Most Common Day Is : " + str(comm_day))

    # TO DO: display the most common start hour
    #get the hour from Start Time to create new column
    df['hour'] = df['Start Time'].dt.hour
    comm_sHour = df['hour'].mode()[0]
    print("The Most Common Start Hour Is : " + str(comm_sHour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    comm_sStation = df['Start Station'].mode()[0]
    print("The Most Common Start Station Is : " + str(comm_sStation))


    # TO DO: display most commonly used end station
    comm_eStation = df['End Station'].mode()[0]
    print("The Most Common End Station Is : " + str(comm_eStation))

    # TO DO: display most frequent combination of start station and end station trip
    #concatenation the two frames together 
    df['comm_StoEtrip'] = df['Start Station'] + " To " + df['End Station']
    print("The Most Common Start to End Station Trip Is : From " + str(df['comm_StoEtrip'].mode()[0]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #Calculate sum of tranel time
    tot_travel_time = df['Trip Duration'].sum()
    print("Total Travel Time Is : " + str(tot_travel_time))

    # TO DO: display mean travel time
    #Calculate the average travel time 
    avg_travel_time = df['Trip Duration'].mean()
    print("The Average Of Travel Time Is : " + str(avg_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#here i need an extra argument (city) because in my dataset 'washington city ' doesn't have any information about gender and year of birth so i need the city argument to avoids error or wrong data to user (specify that the washington city Doesnot have this data)
def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    #to_frame() passed the series name if it have one 
    user_type = df['User Type'].value_counts().to_frame()
    print("Number of User Types Are : " + str(user_type))
    # TO DO: Display counts of gender
    if city == 'chicago' or city == 'new york city' :
        gend_count = df['Gender'].value_counts().to_frame()
        print ("The Count Of Gender = " + str(gend_count))
    
    # TO DO: Display earliest, most recent, and most common year of birth
        earl_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        comm_year = int(df['Birth Year'].mode()[0])
        print("The Earliest Year Of Birth Is : " + str(earl_year))
        print("The Most Recent Year Of Birth Is : " + str(recent_year))
        print("The Most Common Year Of Birth Is : " + str(comm_year))
    else:
              
            print("The Washington City Doesn't Have Any Data About Year Of Birth")      
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)
# this function is to ask the user about if he want to display a 5 raw of data about the city he choose 
def display_raw_data(df):
    disp_raw = input("There is  5 Raw Data Is Available To Display , Display It ? (Yes , No ) ").lower()
    i=0
    #check for invalid input
    if disp_raw not in  ['yes','no']:
        print("Invalid Input")
        disp_raw = input("There is  5 Raw Data Is Available To Display , Display It ? (Yes , No ) ").lower()
    # user doesnt want to display data
    elif disp_raw != 'yes':
        print("Always Here To Help")
    else :
        #Return representing the dimensionality of the dataframe.
        while i+5 < df.shape[0]:
            #to access a location of a specific cell 
            print(df.iloc[i:i+5])
            i += 5
            disp_raw = input("would you like To Display Another 5 Raw Data , Display It ? (Yes , No ) ").lower()
            if disp_raw != 'yes':
                print("Always Here To Help")
                break
        



            
            
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("My Regards , Bye until seeing you again")
            break


if __name__ == "__main__":
	main()
