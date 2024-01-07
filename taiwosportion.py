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