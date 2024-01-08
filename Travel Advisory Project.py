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
        if newsData['articles'] == []: # Check if there are no articles for the selected country
          with open('countries.txt', 'a') as file:
            file.write('\n \n no top headlines today for this country! Try again later \n \n')
        else:  # If there are articles, proceed to process and write them to the 'countries.txt' file
          #check the input vallidity of a country with spaces such as united kingdom
          #pp(newsData)
          with open('countries.txt', 'a') as file:  # Open 'countries.txt' file in append mode
            articles = newsData.get('articles', [])  # Retrieve the list of articles from the JSON data
            file.write('these are the top headlines on the country of choice today:'+'\n'+ '\n'+ '\n')# Write a header to the file indicating that these are the top headlines for the selected country today

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
  