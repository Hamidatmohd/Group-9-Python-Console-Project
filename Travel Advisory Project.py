from pip._vendor import requests   #imports the requests library
from pprint import pprint as pp    #imports the pretty print library

#creation of a class called tripInformation
class tripInformation:

#creation of an init method that accepts user input as a parameter
#if no input is passed as a parameter, then user is asked for input
    
  def __init__(self, userInput=''):
      self.userInput = userInput if userInput else input('Enter the name of the country you wish to travel to: ')

  #api call for countries, to get information from the rest couuntry api

  def getGeneralInfo(self):
    formatCountryName = self.userInput.replace(' ', '%20')   #addes %20 into the endpoint url to replace spaces
    countryUrl = 'https://restcountries.com/v3.1/name/{name}'.format(name = formatCountryName) #endpoint
    response = requests.get(countryUrl) #making a call to the api
    checkConnection = response.status_code  #gets the status code and stores it to a variable