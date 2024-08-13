import requests
#C1. Create a class with instance variables. 
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
    #C2. Create a method for each of the following variables: mean temp in Fahrenheit, max wind speed in mph, precipitation sum in inches
    def fetch_temperature(self):
        temperatures = []
        for year in range(self.year - 4, self.year + 1):
            url = f"https://archive-api.open-meteo.com/v1/archive?latitude={self.latitude}&longitude={self.longitude}&start_date={year}-{self.month:02d}-{self.day:02d}&end_date={year}-{self.month:02d}-{self.day:02d}&daily=temperature_2m_mean&temperature_unit=fahrenheit&timezone=America%2FNew_York"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                temperatures.append(data['daily']['temperature_2m_mean'][0])
        
        if temperatures:
            self.averagetemp = sum(temperatures) / len(temperatures)
            self.mintemp = min(temperatures)
            self.maxtemp = max(temperatures)
    
    def fetch_wind_speed(self):
        wind_speeds = []
        for year in range(self.year - 4, self.year + 1):
            url = f"https://archive-api.open-meteo.com/v1/archive?latitude={self.latitude}&longitude={self.longitude}&start_date={year}-{self.month:02d}-{self.day:02d}&end_date={year}-{self.month:02d}-{self.day:02d}&daily=windspeed_10m_max&wind_speed_unit=mph&timezone=America%2FNew_York"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                wind_speeds.append(data['daily']['windspeed_10m_max'][0])
        
        if wind_speeds:
            self.averagewind = sum(wind_speeds) / len(wind_speeds)
            self.minwind = min(wind_speeds)
            self.maxwind = max(wind_speeds)
    
    def fetch_precipitation(self):
        precipitations = []
        for year in range(self.year - 4, self.year + 1):
            url = f"https://archive-api.open-meteo.com/v1/archive?latitude={self.latitude}&longitude={self.longitude}&start_date={year}-{self.month:02d}-{self.day:02d}&end_date={year}-{self.month:02d}-{self.day:02d}&daily=precipitation_sum&precipitation_unit=inch&timezone=America%2FNew_York"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                precipitations.append(data['daily']['precipitation_sum'][0])
        
        if precipitations:
            self.sumprecip = sum(precipitations)
            self.minprecip = min(precipitations)
            self.maxprecip = max(precipitations)
    
    def display_data(self):
        print(f"5-Year Weather Data for {self.month}/{self.day} in SSM:")
        print(f"Average Temperature: {self.averagetemp} F (Min: {self.mintemp} F, Max: {self.maxtemp} F)")
        print(f"Average Wind Speed: {self.averagewind} mph (Min: {self.minwind} mph, Max: {self.maxwind} mph)")
        print(f"Total Precipitation: {self.sumprecip} inches (Min: {self.minprecip} inches, Max: {self.maxprecip} inches)")

            