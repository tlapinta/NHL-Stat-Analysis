import psycopg2

#Connects to the database
def dbConnect():
    #server connection credentials
    hostname = 'localhost' #Your hostmane
    database = 'dbname' #Your database
    username = 'uname' #Your username
    pwd = 'pwd' #Your password
    port_id = 'port_id' #Your port number

    try:
        con = psycopg2.connect(host = hostname, 
                               dbname = database, 
                               user = username, 
                               password = pwd, 
                               port = port_id)
        print('Connection to server established!')
        return con
    except Exception as e:
        print(f'An error occured: {e}')
        return -1

#Creates a cursor object and checks for errors  
def cursorCreate(connection):
    try:
        cursor = connection.cursor()
        print('Cursor created successfully!')
        return cursor
    except Exception as e:
        print(f"An error occurred: {e}.")
        return -1

#Destroys a cursor object and checks for errors  
def cursorDestroy(cursor):
    try:
        cursor.close()
        print('Cursor closed successfully!')
        return 0
    except Exception as e:
        print(f"An error occurred: {e}.")
        return -1

#Disconnects from the database
def dbDisconnect(connection):
    try:
        connection.close()
        print("Connection to server closed successfully!")
        return 0
    except Exception as e:
        print(f"An error occurred: {e}.")
        return -1