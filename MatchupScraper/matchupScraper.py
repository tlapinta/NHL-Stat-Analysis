import requests
from bs4 import *
from Lib.getDate import *
from Lib.tableExtraction import *
from Lib.dbConnect import *
from Lib.loadMatchups import loadMatchups

def matchupScraper():
    #Sends a get request to the server and records the response
    date = get_Current_Date()
    webpage = 'https://www.cbssports.com/nhl/schedule/' + str(date) + '/'
    response = requests.get(webpage)

    #Code 200 means a successful get request
    if response.status_code == 200:
        #Parses through the page using lxml which is the most efficient way to parse
        #Finds the table based on the first table class found on the page
        print('Established connection to url successfully!')

        soup = BeautifulSoup(response.text, 'lxml')
        table = soup.find('table', class_='TableBase-table')
        matchups = extractTableData(table)

        if (matchups == -1):
            print('Terminating without loading matchups. Function: extractTableData failed.')
            return -1

        con = dbConnect()
        if (con == -1):
            print('Terminating without loading matchups. Failed to establish connection with database.')
            return -1
        
        cursor = cursorCreate(con)
        if (cursor == -1):
            print('Terminating without loading matchups. Failed to establish cursor object.')
            return -1

        lm = loadMatchups(matchups, cursor, con)
        if (lm == -1):
            print('Terminating without loading matchups. Function loadMatchups failed.')
            return -1

        cd = cursorDestroy(cursor)
        dbd = dbDisconnect(con)

        if (cd == -1 or dbd == -1):
            return -1

        return 0
    else:
        print("Error. Could not process GET request to server url:" + str(webpage))
        return -1

