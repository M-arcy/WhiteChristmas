from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class WeatherDataModel(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
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


class WeatherDatabase:
    def __init__(self, db_name="weather_data.db"):
        self.engine = create_engine(f"sqlite:///{db_name}")
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def add_weather_data(self, weather_data):
        session = self.Session()
        try:
            existing = session.query(WeatherDataModel).filter_by(
                latitude=weather_data.latitude,
                longitude=weather_data.longitude,
                month=weather_data.month,
                day=weather_data.day,
                year=weather_data.year,
            ).first()

            if existing is not None:
                print(f"Record for {weather_data.year} already exists. Skipping.")
                return

            record = WeatherDataModel(
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
                max_precipitation=weather_data.maxprecip,
            )
            session.add(record)
            session.commit()
        except Exception as error:
            session.rollback()
            print(f"Error saving record for {weather_data.year}: {error}")
        finally:
            session.close()

    def query_all_data(self):
        session = self.Session()
        try:
            return session.query(WeatherDataModel).all()
        finally:
            session.close()

    def query_data_by_year(self, year):
        session = self.Session()
        try:
            record = session.query(WeatherDataModel).filter_by(year=year).first()
            if record:
                print(f"Weather Data for {record.year}:")
                print(f"  Location: ({record.latitude}, {record.longitude})")
                print(f"  Date: {record.month}/{record.day}/{record.year}")
                print(f"  Avg Temp: {record.avg_temp} F  (Min: {record.min_temp} F, Max: {record.max_temp} F)")
                print(f"  Avg Wind Speed: {record.avg_wind_speed} mph  (Min: {record.min_wind_speed} mph, Max: {record.max_wind_speed} mph)")
                print(f"  Sum Precipitation: {record.sum_precipitation} inches  (Min: {record.min_precipitation} in, Max: {record.max_precipitation} in)")
            else:
                print(f"No data found for {year}.")
        finally:
            session.close()
