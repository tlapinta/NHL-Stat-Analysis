from datetime import *

def get_Current_Date():
    # Get the current date
    current_date = datetime.now()
    
    # Format the date as "yyyymmdd"
    formatted_date = current_date.strftime("%Y%m%d")
    
    return formatted_date