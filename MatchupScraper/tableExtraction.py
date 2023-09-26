from bs4 import *
import sys

def extractTableData(table):
        if table:
            data = []

            # Extract data from the table rows
            for row in table.find_all('tr'):
                # Initialize an empty dictionary for each row
                row_data = {}

                # Extract data from the cells (td elements) in this row
                cells = row.find_all('td')
                if len(cells) >= 2:  # Ensure there are enough cells with data
                    row_data['Away'] = cells[0].get_text(strip=True)
                    row_data['Home'] = cells[1].get_text(strip=True)

                    # Append the row data to the list
                    data.append(row_data)
            
            return 0
        else: 
            print("Error retrieving rows from table", file=sys.stderr)
            return -1
