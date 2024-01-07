# Travel InfoHub Console App

This Python console application is designed to assist prospective travelers in retrieving and displaying information about a specific country using the Rest Countries API, OpenWeather, and the News API. It allows users to input a country name, and fetch details such as the country's name, languages, currencies, and alternative spellings and write this information into a text file. Additionally, the app retrieves news articles related to the specified country and displays their titles, sources, and URLs. This app also helps with the provision of current weather updates of the prospective traveler's choice.

## Prerequisites
- Python 3. x
- `requests` module

## Setup
1. Obtain API keys for the Rest Countries API, OpenWeather API and the News API.
2. Install the `requests` module using the following command:
   ```
   pip install requests
   ```

## Usage
1. Open the terminal or command prompt.
2. Navigate to the directory where the Python script is saved.
3. Run the script using the following command:
   ```
   python country_info_app.py
   ```
4. Enter the name of the country when prompted.
5. The script retrieves and saves this information: 1. country name, languages, currencies 2. Related latest news articles about the country, date of news publications, and URLs in a file named 'countries.txt'

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





