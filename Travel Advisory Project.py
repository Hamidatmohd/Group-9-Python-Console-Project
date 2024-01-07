from pip._vendor import requests   #imports the requests library
from pprint import pprint as pp    #imports the pretty print library

#creation of a class called tripInformation
class tripInformation:

#creation of an init method that accepts user input as a parameter
#if no input is passed as a parameter, then user is asked for input
    
  def __init__(self, userInput=''):
      self.userInput = userInput if userInput else input('Enter the name of the country you wish to travel to: ')

  #api call for countries, to get information from the rest country api

  def getGeneralInfo(self):
    formatCountryName = self.userInput.replace(' ', '%20')   #addes %20 into the endpoint url to replace spaces
    countryUrl = 'https://restcountries.com/v3.1/name/{name}'.format(name = formatCountryName) #endpoint
    response = requests.get(countryUrl) #making a call to the api
    checkConnection = response.status_code  #gets the status code and stores it to a variable

    #api call for getting latest news from countries
  #api key is the same for all free calls
  #apikey= 9e3bd8f42a84440a86fe64d1d56391d4


def getNewsInfo(self):
      # Build the URL for the news API using the provided API key and user input (country)
      newsUrl ='https://newsapi.org/v2/top-headlines?q={country}&apiKey=9e3bd8f42a84440a86fe64d1d56391d4'.format(country = self.userInput) #endpoint

       # Make a GET request to the news API
      response = requests.get(newsUrl)

      # Check if the connection was successful (status code 200)
      checkConnection= response.status_code
      if checkConnection != 200:
        print('error! getting news information from the country')
      else:
        newsData = response.json()

#api call to obtain weather information on the country selected above
def getWeatherInfo(self):
    #remove api - key
    api_key = 'e92f077c81984a46baba3714a1d18d90'

    endpoint = 'http://api.openweathermap.org/data/2.5/weather'

    payload = {
        'unit': 'metrics',
        'appid': api_key
    }
    payload['q'] = self.userInput

    response = requests.get(url= endpoint, params= payload)
    checkConnection= response.status_code
    if checkConnection != 200:
      print('error!, Country does not exist')
    else:
      weatherData=response.json()
      
     # Open the 'countries.txt' file in append mode and use 'file' as the file handle
      with open('countries.txt', 'a') as file:
    
    # Extract the 'main' information from the 'weatherData' dictionary
        mainInfo = weatherData.get('main', {})
        
        # Write introductory information to the file
        file.write('This is the weather forecast for today in the country:'+'\n'+ '\n'+ '\n')
        
        # Iterate through the 'mainInfo' dictionary and write key-value pairs to the file
        for key, value in mainInfo.items():
            file.write(f"{key}: {value}\n")

    # Extract the 'weather' information from the 'weatherData' dictionary
        weatherInfo = weatherData.get('weather', [])

          # A section header for additional weather information to the file
        file.write('\nAdditional Weather Information about the weather:'+'\n'+ '\n'+ '\n')
                    
        for info in weatherInfo:
          for key, value in info.items():
                file.write(f"{key}: {value}\n")

# Create an instance of the 'tripInformation' class
trip = tripInformation()

# Call methods to gather general, news, and weather information for the trip
trip.getGeneralInfo()
trip.getNewsInfo()
trip.getWeatherInfo()