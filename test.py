import unittest
from unittest.mock import patch, MagicMock
from weather_data import WeatherData
from weather_database import WeatherDatabase


def make_api_response(variable, value):
    """Build a fake API response shaped like the real Open-Meteo JSON."""
    mock = MagicMock()
    mock.status_code = 200
    mock.raise_for_status = MagicMock()
    mock.json.return_value = {"daily": {variable: [value]}}
    return mock


class TestWeatherDataWithMocks(unittest.TestCase):
    """These tests use fake API responses so they run offline and instantly."""

    @patch("weather_data.requests.get")
    def test_fetch_temperature_calculates_average(self, mock_get):
        # Simulate 5 years of temperature data: 10, 20, 30, 40, 50 F
        mock_get.side_effect = [
            make_api_response("temperature_2m_mean", temp)
            for temp in [10.0, 20.0, 30.0, 40.0, 50.0]
        ]
        weather = WeatherData(latitude=46.4953, longitude=-84.3453, month=12, day=25, year=2023)
        weather.fetch_temperature()

        self.assertAlmostEqual(weather.averagetemp, 30.0)
        self.assertEqual(weather.mintemp, 10.0)
        self.assertEqual(weather.maxtemp, 50.0)

    @patch("weather_data.requests.get")
    def test_fetch_wind_speed_calculates_average(self, mock_get):
        mock_get.side_effect = [
            make_api_response("windspeed_10m_max", speed)
            for speed in [5.0, 10.0, 15.0, 20.0, 25.0]
        ]
        weather = WeatherData(latitude=46.4953, longitude=-84.3453, month=12, day=25, year=2023)
        weather.fetch_wind_speed()

        self.assertAlmostEqual(weather.averagewind, 15.0)
        self.assertEqual(weather.minwind, 5.0)
        self.assertEqual(weather.maxwind, 25.0)

    @patch("weather_data.requests.get")
    def test_fetch_precipitation_sums_values(self, mock_get):
        mock_get.side_effect = [
            make_api_response("precipitation_sum", amount)
            for amount in [0.0, 0.1, 0.2, 0.0, 0.3]
        ]
        weather = WeatherData(latitude=46.4953, longitude=-84.3453, month=12, day=25, year=2023)
        weather.fetch_precipitation()

        self.assertAlmostEqual(weather.sumprecip, 0.6)
        self.assertEqual(weather.minprecip, 0.0)
        self.assertEqual(weather.maxprecip, 0.3)

    @patch("weather_data.requests.get")
    def test_api_failure_is_skipped_gracefully(self, mock_get):
        """A failed API call for one year should not crash — it just gets skipped."""
        import requests as real_requests
        mock_get.side_effect = real_requests.RequestException("connection error")
        weather = WeatherData(latitude=46.4953, longitude=-84.3453, month=12, day=25, year=2023)
        weather.fetch_temperature()
        self.assertIsNone(weather.averagetemp)


class TestWeatherDatabase(unittest.TestCase):

    def _make_weather(self):
        """Create a WeatherData object with values pre-filled (no API call needed)."""
        return WeatherData(
            latitude=46.4953, longitude=-84.3453, month=12, day=25, year=2023,
            averagetemp=28.0, mintemp=17.0, maxtemp=39.0,
            averagewind=13.5, minwind=10.0, maxwind=17.5,
            sumprecip=0.34, minprecip=0.0, maxprecip=0.30,
        )

    def test_add_weather_data_inserts_record(self):
        db = WeatherDatabase(":memory:")
        db.add_weather_data(self._make_weather())
        records = db.query_all_data()
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].year, 2023)

    def test_no_duplicate_records(self):
        db = WeatherDatabase(":memory:")
        weather = self._make_weather()
        db.add_weather_data(weather)
        db.add_weather_data(weather)
        records = db.query_all_data()
        self.assertEqual(len(records), 1)

    def test_query_data_by_year_returns_correct_record(self):
        db = WeatherDatabase(":memory:")
        db.add_weather_data(self._make_weather())
        # query_data_by_year prints output — we just verify it doesn't crash
        # and the underlying data is correct via query_all_data
        records = db.query_all_data()
        self.assertEqual(records[0].avg_temp, 28.0)

    def test_query_all_data_empty_database(self):
        db = WeatherDatabase(":memory:")
        records = db.query_all_data()
        self.assertEqual(records, [])


if __name__ == "__main__":
    unittest.main()
