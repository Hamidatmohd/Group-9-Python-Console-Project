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
https://newsapi.org/ for retrieving the latest news articles

## Code Explanation
- The script uses the `requests` module to send HTTP requests to the Rest Countries API and the News API.
- The API keys for the Rest Countries API and the News API are stored in variables named `rest_countries_api_key` and `news_api_key`, respectively.
- The `get_country_info` function retrieves country information from the Rest Countries API and returns a dictionary containing details such as the country's name, capital, population, region, and subregion.
- The `write_to_file` function writes the country information to a text file.
- The `get_country_news` function retrieves news related to a specific country from the News API and returns a list of articles.
- The `main` function serves as the application's entry point, where users can input the country name, and the app retrieves and displays the country information and news articles.

## To reuse the code for this application, note the following 
- Ensure that valid API keys for the Rest Countries API and the News API are obtained and replaced with the placeholder values in the script with the actual API keys.
- The script will create a text file containing the country information in the same directory where the script is executed.





