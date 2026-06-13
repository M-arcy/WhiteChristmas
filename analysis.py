"""
White Christmas probability analysis for Sault Ste. Marie, Michigan.

Loads weather data from the SQLite database, computes a white christmas
likelihood estimate, and prints a summary. The same logic is also shown
step-by-step in the accompanying Jupyter notebook.
"""

import sqlite3
import pandas as pd

PRECIPITATION_THRESHOLD_INCHES = 0.0  # any precip above zero counts as measurable
FREEZING_FAHRENHEIT = 32.0  # average temp must be at or below this for snow to be likely
DB_PATH = "weather_data.db"  # path to the local SQLite database file


def load_data(db_path=DB_PATH):
    conn = sqlite3.connect(db_path)  # connect to the SQLite database
    df = pd.read_sql_query("SELECT * FROM weather_data ORDER BY year", conn)  # load all records into a DataFrame, sorted by year
    conn.close()  # always close the connection when done
    return df


def add_derived_columns(df):
    df = df.copy()  # work on a copy so we don't modify the original DataFrame
    df["had_precipitation"] = df["sum_precipitation"] > PRECIPITATION_THRESHOLD_INCHES  # True if any precipitation was recorded that day
    df["was_freezing"] = df["avg_temp"] <= FREEZING_FAHRENHEIT  # True if average temperature was at or below 32 F
    df["likely_white_christmas"] = df["had_precipitation"] & df["was_freezing"]  # both conditions must be true for a likely white christmas
    return df


def print_summary(df):
    total_years = len(df)  # total number of years in the dataset
    years_with_precip = df["had_precipitation"].sum()  # count of years with measurable precipitation
    years_freezing = df["was_freezing"].sum()  # count of years where average temp was freezing or below
    years_white = df["likely_white_christmas"].sum()  # count of years meeting both white christmas conditions

    precip_pct = years_with_precip / total_years * 100  # percentage of years with precipitation
    white_pct = years_white / total_years * 100  # estimated white christmas probability as a percentage

    print("=" * 50)
    print("White Christmas Analysis — Sault Ste. Marie, MI")
    print("=" * 50)
    print(f"Years analyzed: {df['year'].min()} – {df['year'].max()} ({total_years} years)")
    print()
    print(f"Years with measurable precipitation on Dec 25: {years_with_precip}/{total_years} ({precip_pct:.0f}%)")
    print(f"Years where average temp was at or below freezing: {years_freezing}/{total_years}")
    print()
    print(f"Likely white christmases (precipitation AND freezing): {years_white}/{total_years}")
    print(f"Estimated probability of a white christmas: {white_pct:.0f}%")
    print()
    print("Year-by-year breakdown:")
    for _, row in df.iterrows():  # loop through each row and print a one-line summary
        label = "White Christmas" if row["likely_white_christmas"] else "Not white"
        print(f"  {int(row['year'])}: avg temp {row['avg_temp']:.1f} F, "
              f"precip {row['sum_precipitation']:.3f} in — {label}")
    print("=" * 50)
    print()
    print("Note: this uses average daily temperature as a freezing proxy.")
    print("Snowfall data (not collected) would give a more precise answer.")


if __name__ == "__main__":
    df = load_data()  # load data from the database
    df = add_derived_columns(df)  # calculate the white christmas columns
    print_summary(df)  # display the results
