import unittest
from weather_data import WeatherData
from weather_database import WeatherDatabase

class TestWeatherData(unittest.TestCase):
    def test_fetch_temperature(self):
        weather = WeatherData(latitude=46.4953, longitude=-84.3453, month=12, day=25, year=2023)
        weather.fetch_temperature()
        self.assertIsNotNone(weather.averagetemp, "Average temperature should not be None")
        self.assertGreater(weather.averagetemp, -100, "Average temperature should be greater than -100 F")
        self.assertLess(weather.averagetemp, 150, "Average temperature should be less than 150 F")

class TestWeatherDatabase(unittest.TestCase):
    def test_add_weather_data(self):
        db = WeatherDatabase(":memory:")  # Use an in-memory database for testing
        weather = WeatherData(latitude=46.4953, longitude=-84.3453, month=12, day=25, year=2023)
        weather.fetch_temperature()
        weather.fetch_wind_speed()
        weather.fetch_precipitation()
        db.add_weather_data(weather)
        records = db.query_all_data()
        self.assertEqual(len(records), 1, "There should be exactly one record in the database")
        self.assertEqual(records[0].year, 2023, "The record should be for the year 2023")

    def test_no_duplicate_records(self):
        db = WeatherDatabase(":memory:")  # Use an in-memory database for testing
        weather = WeatherData(latitude=46.4953, longitude=-84.3453, month=12, day=25, year=2023)
        weather.fetch_temperature()
        weather.fetch_wind_speed()
        weather.fetch_precipitation()
        db.add_weather_data(weather)
        db.add_weather_data(weather)  # Attempt to add the same record again
        records = db.query_all_data()
        self.assertEqual(len(records), 1, "There should be only one record in the database after attempting to add a duplicate")
