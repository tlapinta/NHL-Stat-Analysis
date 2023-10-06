import psycopg2
import os
from dotenv import load_dotenv

#Connects to the database
def dbConnect(filename):
    #Loads the env file
    curr_dir = os.path.dirname(__file__)
    path = os.path.join(curr_dir, '../Env/db.env')
    load_dotenv(path)

    #server connection credentials from env file
    hostname = os.getenv('host')
    database = os.getenv('DB')
    username = os.getenv('uname')
    pwd = os.getenv('password')
    port_id = int(os.getenv('portID'))

    try:
        con = psycopg2.connect(host = hostname, 
                               dbname = database, 
                               user = username, 
                               password = pwd, 
                               port = port_id)
        print('Connection to server established!')
        filename.write('Connection to server established!\n')
        return con
    except Exception as e:
        print(f'An error occured: {e}')
        filename.write('An error occured: ' + str(e) + '\n')
        return -1

#Creates a cursor object and checks for errors  
def cursorCreate(connection, filename):
    try:
        cursor = connection.cursor()
        print('Cursor created successfully!')
        filename.write('Cursor created successfully!\n')
        return cursor
    except Exception as e:
        print(f"An error occurred: {e}.")
        filename.write('An error occured: ' + str(e) + '\n')
        return -1

#Destroys a cursor object and checks for errors  
def cursorDestroy(cursor, filename):
    try:
        cursor.close()
        print('Cursor closed successfully!')
        filename.write('Cursor closed successfully!\n')
        return 0
    except Exception as e:
        print(f"An error occurred: {e}.")
        filename.write('An error occured: ' + str(e) + '\n')
        return -1

#Disconnects from the database
def dbDisconnect(connection, filename):
    try:
        connection.close()
        print("Connection to server closed successfully!")
        filename.write('Connection to server closed successfully!\n')
        return 0
    except Exception as e:
        print(f"An error occurred: {e}.")
        filename.write('An error occured: ' + str(e) + '\n')
        return -1