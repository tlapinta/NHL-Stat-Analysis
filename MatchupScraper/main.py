from matchupScraper import *
from datetime import *
import os

def main():
    #Creates log file to store the stack trace and errors
    curr_path = os.path.dirname(__file__)
    log_path = curr_path + '\Logs\load_' + str(date.today()) +'.txt'
    log_file = open(log_path, 'w')

    #Starts the program
    print('Starting matchup scraper...')
    log_file.write('Starting matchup scraper...\n')
    ret = matchupScraper(log_file)
    if (ret == -1):
        print('Process completed with errors.')
        log_file.write('Process completed with errors.\n')
    else:
        print('Process completed successfully!')
        log_file.write('Process completed successfully!\n')
    log_file.close()
    return 0
        
#Main Method
if __name__ == '__main__':
    main()