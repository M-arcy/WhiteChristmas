


# WhiteChristmas

## Table of Contents

- [Description](#description)
- [Visuals](#visuals)
- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)
- [Roadmap](#roadmap)
- [Contribute](#contribute)
- [Author](#author)

<hr style="border: none; height: 3px; background-color: #003057;" />

## Name

White Christmas Weather Analysis and Database

## Description

WhiteChristmas is a __Python__-based project designed to retrieve and analyze historical weather data for a specific location on a specific date over the past five years. For the purposes of this project, the data collection focuses on Christmas Day in Sault Ste. Marie, Michigan, and uses an __external weather API__ to gather data, which is then stored in an __SQLite database__. The application is designed in general to assist event planners in understanding weather patterns and making informed decisions for outdoor event planning. This project happens to accompany another project repository that covers machine learning for the same city and date. It can be found at [Github.com/M-arcy](http://github.com/M-arcy/Will-There-Be-a-White-Christmas-this-Year-in-Sault-Michigan).

The project includes methods to fetch and display temperature, wind speed, and precipitation data, as well as store this information in a local SQLite database using SQLAlchemy. The project ensures data integrity by avoiding duplicate entries and provides a method to query and display data for any given year.


This project has these files:
 - 'weather_data.py'  - contains the 'WeatherData' class, for fetching weather data from the Open-Meteo API. 
 - 'weather_database.py'  - defines the 'WeatherDatabase' class and manages SQLite database interactions using the SQLAlchemy ORM model.
 - 'main.py' -  serves as the entry point for the project coordinating data retrieval, storage and querying.  
 - 'test.py' -  contains unit tests for the project, ensuring key functionalities work as expected. 
 - 'requirements.txt' -  lists all the packages and dependencies required to run the project. 
 - 'README.md'  - provides an overview of the project. 


## Badges

![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

## Visuals

Here's an example of the output generated:
```go
5-Year Weather Data for 12/25 in SSM:
Average Temperature: 28.18 F (Min: 17.0 F, Max: 39.4 F)
Average Wind Speed: 13.5 mph (Min: 10.3 mph, Max: 17.5 mph)
Total Precipitation: 0.339 inches (Min: 0.0 inches, Max: 0.303 inches)
```

## Installation

To set up this project on your local machine, follow these steps:

Clone the repository:

```go
git clone https://github.com/YourUsername/WhiteChristmas.git
cd WhiteChristmas 
```

Create and activate a virtual environment (optional but recommended):

```python
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required dependencies:

```python
pip install -r requirements.txt

```

## Usage

To use the WhiteChristmas project:

Run the main script to fetch and store weather data:

```python
python main.py
```

Query the stored data for a specific year. Modify the main.py script or use the provided query method to retrieve and display data for any specific year.

## Support

For support, you can open an issue on the GitHub repository or contact the author via email at mmisn15@wgu.edu.

## Roadmap

Future enhancements may include:

* Expanding the data retrieval to include more locations for a regional prediction.
* Adding more weather metrics such as snowfall amounts.
* Implementing a web-based interface for easier access to the data.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

* Fork the repository.
* Create a new branch (__git checkout -b feature-branch__).
* Make your changes.
* Commit your changes (__git commit -m 'Add new feature'__).
* Push to the branch (__git push origin feature-branch__).
* Open a Pull Request.

## Authors and acknowledgment

This project was developed by __Marcy Misner__. Special thanks to the open-source community for the libraries and tools used in this project.
For more examples of my work, see my [Github portfolio](https://github.com/M-arcy) and my [LinkedIn profile](https://www.linkedin.com/in/marcy-misner/).

## License

This project is licensed under the MIT License.

## Project status

This project is actively maintained for the next six months. Future updates and features within that time frame are planned. Contributions and suggestions are always welcome.


