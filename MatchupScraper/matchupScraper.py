from bs4 import *
from getDate import *
from tableExtraction import *
import requests
import sys

def matchupScraper():
    #Sends a get request to the server and records the response
    date = get_Current_Date()
    webpage = 'https://www.cbssports.com/nhl/schedule/' + str(date) + '/'
    response = requests.get(webpage)

    #Code 200 means a successful get request
    if response.status_code == 200:
        #Parses through the page using lxml which is the most efficient way to parse
        #Finds the table based on the first table class found on the page
        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find('table', class_='TableBase-table')
        extractTableData(table)
        return 0
    else:
        print("Error. Could not process GET request to server url:" + str(webpage), file=sys.stderr)
        return -1

