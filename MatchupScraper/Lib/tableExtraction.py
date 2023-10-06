from datetime import *
from bs4 import *

def extractTableData(table, filename):
        if table:
            try:
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
                        row_data['Date'] = datetime.now()

                        # Append the row data to the list
                        data.append(row_data)

                return data
            except Exception as e:
                print(f"Error extracting HTML data from table. Error: {e}")
                filename.write('Error extracting HTML data from table. Error: ' + str(e))
                return -1
        else: 
            print("Error table object does not exist.")
            filename.write('Error table object does not exist.\n')
            return -1
