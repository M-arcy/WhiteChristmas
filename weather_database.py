""" C4.  Write a second class that creates a table in SQLite using the SQLAlchemy ORM module. Include a field for each of the following instance variables in the table:

•   primary key

•   location latitude

•   location longitude

•   month

•   day of month

•   year

•   five-year average temperature on chosen date

•   five-year minimum temperature on chosen date

•   five-year maximum temperature on chosen date

•   five-year average wind speed on chosen date

•   five-year minimum wind speed on chosen date

•   five-year maximum wind speed on chosen date

•   five-year sum precipitation on chosen date

•   five-year minimum precipitation on chosen date

•   five-year maximum precipitation on chosen date """

""" C6.  Write a method that queries the table you created in SQLite and retrieves the data you stored in part C5. Include a screenshot that shows the formatted version of the data on the screen for your chosen location and date. 
The screenshot must be clear and show the full view of your screen, including the date and time."""

from sqlalchemy import create_engine, Column, Integer, Float, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a base class for declarative models
Base = declarative_base()


# Define the WeatherDataModel class to map to the SQLite table, creates the table with column headers
class WeatherDataModel(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Primary key
    latitude = Column(Float)
    longitude = Column(Float)
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)
    avg_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)
    avg_wind_speed = Column(Float)
    min_wind_speed = Column(Float)
    max_wind_speed = Column(Float)
    sum_precipitation = Column(Float)
    min_precipitation = Column(Float)
    max_precipitation = Column(Float)


# Per C4, create a new class to handle database operations
class WeatherDatabase:
    def __init__(self, db_name='weather_data.db'):
        # Create a SQLite engine
        self.engine = create_engine(f'sqlite:///{db_name}')
        Base.metadata.create_all(self.engine)  # Create all tables
        self.Session = sessionmaker(bind=self.engine)

    def add_weather_data(self, weather_data):
        session = self.Session()
        try:
            # Check if the record for this year already exists
            existing_record = session.query(WeatherDataModel).filter_by(
                latitude=weather_data.latitude,
                longitude=weather_data.longitude,
                month=weather_data.month,
                day=weather_data.day,
                year=weather_data.year
            ).first()

            if existing_record is None:  # Only adds if the record doesn't already exist so there's no duplicates
                weather_record = WeatherDataModel(
                    latitude=weather_data.latitude,
                    longitude=weather_data.longitude,
                    month=weather_data.month,
                    day=weather_data.day,
                    year=weather_data.year,
                    avg_temp=weather_data.averagetemp,
                    min_temp=weather_data.mintemp,
                    max_temp=weather_data.maxtemp,
                    avg_wind_speed=weather_data.averagewind,
                    min_wind_speed=weather_data.minwind,
                    max_wind_speed=weather_data.maxwind,
                    sum_precipitation=weather_data.sumprecip,
                    min_precipitation=weather_data.minprecip,
                    max_precipitation=weather_data.maxprecip
                )
                session.add(weather_record)
                session.commit()  # Commit the transaction
            else:
                print(f"Record for {weather_data.year} already exists. Skipping insertion.")
        except Exception as e:
            session.rollback()  # Roll back the transaction on error
            print(f"Failed to add weather data: {e}")
        finally:
            session.close()  # Close the session

    def query_all_data(self):
        # Create a new session
        session = self.Session()
        try:
            # Query all records in the weather_data table
            records = session.query(WeatherDataModel).all()
            return records
        finally:
            session.close()  # Close the session per best practice

    def query_data_by_year(self, year):
        session = self.Session()
        try:
            # Query the record for the specified year
            record = session.query(WeatherDataModel).filter_by(year=year).first()
            if record:
                print(f"Weather Data for {record.year}:")
                print(f"Location: ({record.latitude}, {record.longitude})")
                print(f"Date: {record.month}/{record.day}/{record.year}")
                print(f"Avg Temp: {record.avg_temp} F")
                print(f"Min Temp: {record.min_temp} F")
                print(f"Max Temp: {record.max_temp} F")
                print(f"Avg Wind Speed: {record.avg_wind_speed} mph")
                print(f"Min Wind Speed: {record.min_wind_speed} mph")
                print(f"Max Wind Speed: {record.max_wind_speed} mph")
                print(f"Sum Precipitation: {record.sum_precipitation} inches")
                print(f"Min Precipitation: {record.min_precipitation} inches")
                print(f"Max Precipitation: {record.max_precipitation} inches")
            else:
                print(f"No data found for the year {year}.")
        finally:
            session.close()



