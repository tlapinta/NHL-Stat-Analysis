from matchupScraper import *

#Main Method
if __name__ == '__main__':
    print('Starting matchup scraper...')
    ret = matchupScraper()
    if (ret == -1):
        print('Process completed with errors.')
    else:
        print('Process completed successfully!')