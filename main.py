
#C3.  Create a main.py file type and, within the file, create an instance of the class in part C1 to call the methods used in part C2 for the daily weather variables.
from weather_data import WeatherData as wd
from weather_database import WeatherDatabase  # adding now that database has been created


def main():
    db = WeatherDatabase()  # Initialize the database
    
    for year in range(2019, 2024):  # Loop over the last 5 years and add each to database
        weather = wd(latitude=46.4953, longitude=-84.3453, month=12, day=25, year=year)
        weather.fetch_temperature()
        weather.fetch_wind_speed()
        weather.fetch_precipitation()
        
        # Display the results 
        weather.display_data()
        
        # Add the weather data to the database
        db.add_weather_data(weather)
    
    # Query all data and print it
    records = db.query_all_data()
    for record in records:
        print(record)
    # Example: Query and display data for the year 2023
    db.query_data_by_year(2023)


if __name__ == "__main__":
    main()
