# WhiteChristmas

## Table of Contents

- [Description](#description)
- [Visuals](#visuals)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

<hr style="border: none; height: 10px; background-color: #003057;" />

## Name

White Christmas Weather Analysis and Database

## Description

WhiteChristmas is a **Python**-based project that retrieves and analyzes historical weather data for Christmas Day (December 25) in Sault Ste. Marie, Michigan. It uses the free [Open-Meteo Archive API](https://open-meteo.com/) to collect temperature, wind speed, and precipitation data across a five-year window for any given year, then stores the results in a local **SQLite** database.

The goal is to help answer the question: *based on past weather patterns, is a white Christmas likely in Sault Ste. Marie?* A "white Christmas" here means measurable precipitation (snow or rain) recorded on December 25th.

This project accompanies a companion machine learning repository that builds a prediction model from the same data:
[github.com/M-arcy/Will-There-Be-a-White-Christmas-this-Year-in-Sault-Michigan](https://github.com/M-arcy/Will-There-Be-a-White-Christmas-this-Year-in-Sault-Michigan)

### Project Files

| File | Purpose |
|---|---|
| `weather_data.py` | `WeatherData` class — fetches data from the Open-Meteo API |
| `weather_database.py` | `WeatherDatabase` class — manages SQLite storage via SQLAlchemy ORM |
| `main.py` | Entry point — coordinates data retrieval, storage, and display |
| `test.py` | Unit tests for core functionality |
| `weather_data.db` | Pre-populated SQLite database with data for 2019–2023 |
| `requirements.txt` | Python package dependencies |
| `SQLite query.sql` | Reference SQL query for manual database inspection |

## Badges

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

## Visuals

Example output from running `python main.py`:

```
5-Year Weather Data for 12/25 in SSM:
Average Temperature: 28.18 F (Min: 17.0 F, Max: 39.4 F)
Average Wind Speed: 13.5 mph (Min: 10.3 mph, Max: 17.5 mph)
Total Precipitation: 0.339 inches (Min: 0.0 inches, Max: 0.303 inches)
```

## Installation

Clone the repository:

```bash
git clone https://github.com/M-arcy/WhiteChristmas.git
cd WhiteChristmas
```

Create and activate a virtual environment (recommended):

```bash
python -m venv venv
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

> **Note:** A pre-populated database (`weather_data.db`) is included in the repository. You can query it immediately without running the data-fetch step.

## Usage

**Run the full pipeline** (fetch data from the API and store it in the database):

```bash
python main.py
```

The script loops through years 2019–2023, fetches weather data for each Christmas Day, stores it (skipping duplicates), and prints a summary.

**Run the tests:**

```bash
python -m unittest test.py
```

**Query the database manually** using the provided SQL file as a reference with any SQLite browser (e.g., [DB Browser for SQLite](https://sqlitebrowser.org/)).

## Support

Open an issue on the [GitHub repository](https://github.com/M-arcy/WhiteChristmas/issues) or reach out via [LinkedIn](https://www.linkedin.com/in/marcy-misner/).

## Roadmap

Potential future enhancements:

- Expand data collection to additional locations for regional comparison
- Add snowfall-specific metrics (currently precipitation includes all types)
- Build a web-based interface for interactive querying

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Open a Pull Request

## Author

Developed by **Marcy Misner**.

For more of my work: [GitHub](https://github.com/M-arcy) | [LinkedIn](https://www.linkedin.com/in/marcy-misner/)

## License

This project is licensed under the MIT License.

[Back to Top](#table-of-contents)
