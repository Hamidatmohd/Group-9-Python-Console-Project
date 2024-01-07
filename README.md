# Travel InfoHub Console App

This Python console application is designed to assist prospective travelers in retrieving and displaying information about a specific country using the Rest Countries API, OpenWeather, and the News API. It allows users to input a country name, and fetch details such as the country's name, languages, currencies, and alternative spellings and write this information into a text file. Additionally, the app retrieves news articles related to the specified country and displays their titles, sources, and URLs. This app also helps with the provision of current weather updates of the prospective traveler's choice.

## Prerequisites
- Python 3. x
- `requests` module and pprints

## Setup
1. Obtain API keys for the Rest Countries API, OpenWeather API, and the News API.
## Installation
1. Clone the repository to your local machine
2. Install the needed Python packages using the following command: 
   ```
   pip install requests 
   pip._vendor
   pprint import pprint as pp
   ```

## Usage
1. Navigate to the directory where the Python script tripInformation.py is saved.
2. Run the script in a Python environment, if this is properly executed, the application prompts the user to enter the country name they want to retrieve information on.
3. Enter the name of the country when prompted.
4. The application script retrieves, displays, and saves this information for the specified country:
    i. country name, languages, and currencies
   ii. Related latest news headlines about the country, date of news publications, URLs, and the current weather forecast in a file named 'countries.txt'

# The script requires access to the following APIs:
https://restcountries.com/ for general country information.
https://newsapi.org/v2/top-headlines for retrieving the latest news articles
https://api.openweathermap.org/data/2.5/weather for weather forecast

## Code Explanation
- The 'tripInformation' class comprises methods for retrieving general country information, weather, and news data.
- The `main` function:(tripInformation, trip.getGeneralInfo, trip.getNewsInfo,
trip.getWeatherInfo) serves as the application's entry point, where users can input the country name, and the app retrieves and displays the country information, weather forecast, and news articles.

## File Output
The retrieved information is written in a file named 'countries.txt' and it is found in the same directory where the Python script is stored.

## To reuse the code for this application, note the following 
- Ensure that valid API keys for the Rest Countries API and the News API are obtained and replaced with the placeholder values in the script with the actual API keys.
- The script will create a text file containing the country information in the same directory where the script is executed.





