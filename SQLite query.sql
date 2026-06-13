-- Reference query for manual inspection of the weather_data table.
-- Open weather_data.db in any SQLite browser (e.g. DB Browser for SQLite) and run this.

SELECT id, latitude, longitude, month, day, year,
       avg_temp, min_temp, max_temp,
       avg_wind_speed, min_wind_speed, max_wind_speed,
       sum_precipitation, min_precipitation, max_precipitation
FROM weather_data
ORDER BY year ASC;
