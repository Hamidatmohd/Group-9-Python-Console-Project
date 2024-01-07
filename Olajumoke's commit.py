from pip._vendor import requests
from pprint import pprint as pp
#import json

def getGeneralInfo(self):
    formatCountryName = self.userInput.replace(' ', '%20')
    countryUrl = 'https://restcountries.com/v3.1/name/{name}'.format(name = formatCountryName) #endpoint
    response = requests.get(countryUrl) # Make API call to retrieve country data
    checkConnection = response.status_code # Check the status code of the response
    if checkConnection != 200:
      print('error!, country name is invalid or spelled incorrectly, check again') # Print error message if the request failed
    else:
      countryData = response.json() # Retrieve country data if the request was successful
      with open('countries.txt', 'w') as file: # Open a text file to write the country information
        file.write('These are some of the basic facts on the country:'+'\n'+ '\n'+ '\n') # write header
        #Iterate through each country in the response data
        for i in countryData:
          file.write('Name: ' + str(i.get('name')) + '\n') # Write the country's name to the file and creates a new line
          file.write('Languages: ' + str(i.get('languages')) + '\n') # Write the country's languages to the file
          file.write('Currencies: ' + str(i.get('currencies')) + '\n') # Write the country's currencies to the file
          file.write('Alt Spellings: ' + str(i.get('altSpellings')) + '\n\n') # Write the country's alternative spellings to the file and creates two new lines in the file
