from pip._vendor import requests
from pprint import pprint as pp
#import json

class tripInformation:

  def __init__(self, userInput=''):
      self.userInput = userInput if userInput else input('Enter the name of the country you wish to travel to: ')

  #api call for countries

  def getGeneralInfo(self):
    formatCountryName = self.userInput.replace(' ', '%20')
    countryUrl = 'https://restcountries.com/v3.1/name/{name}'.format(name = formatCountryName) #endpoint
    response = requests.get(countryUrl) #making a call to the api
    checkConnection = response.status_code
    if checkConnection != 200:
      print('error!, country name is invalid or spelled incorrectly, check again')
    else:
      countryData = response.json()
      with open('countries.txt', 'w') as file:
        file.write('These are some of the basic facts on the country:'+'\n'+ '\n'+ '\n')
        for i in countryData:
          file.write('Name: ' + str(i.get('name')) + '\n')
          file.write('Languages: ' + str(i.get('languages')) + '\n')
          file.write('Currencies: ' + str(i.get('currencies')) + '\n')
          file.write('Alt Spellings: ' + str(i.get('altSpellings')) + '\n\n')


  #api call for getting latest news from countries
  #api key is the same for all free calls
  #apikey= 9e3bd8f42a84440a86fe64d1d56391d4


  def getNewsInfo(self):
      newsUrl ='https://newsapi.org/v2/top-headlines?q={country}&apiKey=9e3bd8f42a84440a86fe64d1d56391d4'.format(country = self.userInput) #endpoint

      response = requests.get(newsUrl)
      checkConnection= response.status_code
      if checkConnection != 200:
        print('error! getting news information from the country')
      else:
        newsData = response.json()
        if newsData['articles'] == []: 
          with open('countries.txt', 'a') as file:
            file.write('\n \n no top headlines today for this country! Try again later \n \n')
        else: 
          #check the input vallidity of a country with spaces such as united kingdom
          #pp(newsData)
          with open('countries.txt', 'a') as file:
            articles = newsData.get('articles', [])  # Retrieve the list of articles from the JSON data
            file.write('these are the top headlines on the country of choice today:'+'\n'+ '\n'+ '\n')
            for article in articles:
              # Write the title of the article
              file.write(f"Title: {article['title']}\n")
              # Write the author of the article
              file.write(f"Author: {article['author']}\n")
              # Write the description of the article
              file.write(f"Description: {article['description']}\n")
              # Write the published date of the article
              file.write(f"Published At: {article['publishedAt']}\n")
               # Write the URL of the article
              file.write(f"URL: {article['url']}\n")
              # Write the URL to the image associated with the article
              file.write(f"URL to Image: {article['urlToImage']}\n")
              # Write the content of the article
              file.write(f"Content: {article['content']}\n\n")


  #weatherApi

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
      with open('countries.txt', 'a') as file:
          mainInfo = weatherData.get('main', {})
          file.write('This is the weather forecast for today in the country:'+'\n'+ '\n'+ '\n')
          for key, value in mainInfo.items():
              file.write(f"{key}: {value}\n")
      
      
trip = tripInformation()

trip.getGeneralInfo()
trip.getNewsInfo()
trip.getWeatherInfo()