import requests

YEARS_OF_HISTORY = 5
BASE_URL = "https://archive-api.open-meteo.com/v1/archive"


class WeatherData:
    def __init__(self, latitude, longitude, month, day, year,
                 averagetemp=None, mintemp=None, maxtemp=None,
                 averagewind=None, minwind=None, maxwind=None,
                 sumprecip=None, minprecip=None, maxprecip=None):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.averagetemp = averagetemp
        self.mintemp = mintemp
        self.maxtemp = maxtemp
        self.averagewind = averagewind
        self.minwind = minwind
        self.maxwind = maxwind
        self.sumprecip = sumprecip
        self.minprecip = minprecip
        self.maxprecip = maxprecip

    def _fetch_daily_values(self, variable, extra_params):
        """Fetch a single daily weather variable across YEARS_OF_HISTORY years.

        Returns a list of values (one per year). Skips years where the API
        call fails rather than crashing the whole run.
        """
        values = []
        for year in range(self.year - (YEARS_OF_HISTORY - 1), self.year + 1):
            date_str = f"{year}-{self.month:02d}-{self.day:02d}"
            params = {
                "latitude": self.latitude,
                "longitude": self.longitude,
                "start_date": date_str,
                "end_date": date_str,
                "daily": variable,
                "timezone": "America/New_York",
                **extra_params,
            }
            try:
                response = requests.get(BASE_URL, params=params, timeout=10)
                response.raise_for_status()
                data = response.json()
                values.append(data["daily"][variable][0])
            except requests.RequestException as error:
                print(f"Warning: could not fetch data for {date_str} ({error})")
        return values

    def fetch_temperature(self):
        temps = self._fetch_daily_values(
            "temperature_2m_mean",
            {"temperature_unit": "fahrenheit"},
        )
        if temps:
            self.averagetemp = sum(temps) / len(temps)
            self.mintemp = min(temps)
            self.maxtemp = max(temps)

    def fetch_wind_speed(self):
        speeds = self._fetch_daily_values(
            "windspeed_10m_max",
            {"wind_speed_unit": "mph"},
        )
        if speeds:
            self.averagewind = sum(speeds) / len(speeds)
            self.minwind = min(speeds)
            self.maxwind = max(speeds)

    def fetch_precipitation(self):
        precips = self._fetch_daily_values(
            "precipitation_sum",
            {"precipitation_unit": "inch"},
        )
        if precips:
            self.sumprecip = sum(precips)
            self.minprecip = min(precips)
            self.maxprecip = max(precips)

    def display_data(self):
        print(f"5-Year Weather Data for {self.month}/{self.day} in SSM:")
        print(f"Average Temperature: {self.averagetemp} F (Min: {self.mintemp} F, Max: {self.maxtemp} F)")
        print(f"Average Wind Speed: {self.averagewind} mph (Min: {self.minwind} mph, Max: {self.maxwind} mph)")
        print(f"Total Precipitation: {self.sumprecip} inches (Min: {self.minprecip} inches, Max: {self.maxprecip} inches)")
