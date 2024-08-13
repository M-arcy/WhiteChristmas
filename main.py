
#C3.  Create a main.py file type and, within the file, create an instance of the class in part C1 to call the methods used in part C2 for the daily weather variables.

from weather_data import WeatherData as wd

def main():
    # Create an instance of weather data for SSM on Christmas Day
    weather = wd(latitude=46.4953, longitude=-84.3453, month=12, day=25, year=2023)
    
    # Fetch the weather data
    weather.fetch_temperature()
    weather.fetch_wind_speed()
    weather.fetch_precipitation()
    
    # Display the results
    weather.display_data()
#make sure it 
if __name__ == "__main__":
    main()
