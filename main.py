from weather_data import WeatherData
from weather_database import WeatherDatabase

LATITUDE = 46.4953
LONGITUDE = -84.3453
MONTH = 12
DAY = 25
START_YEAR = 2019
END_YEAR = 2023


def main():
    db = WeatherDatabase()

    for year in range(START_YEAR, END_YEAR + 1):
        weather = WeatherData(latitude=LATITUDE, longitude=LONGITUDE, month=MONTH, day=DAY, year=year)
        weather.fetch_temperature()
        weather.fetch_wind_speed()
        weather.fetch_precipitation()
        weather.display_data()
        db.add_weather_data(weather)

    records = db.query_all_data()
    for record in records:
        print(record)

    db.query_data_by_year(2023)


if __name__ == "__main__":
    main()
