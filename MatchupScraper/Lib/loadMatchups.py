def createTable(cur, conn, filename):
    try:
        query = """
            CREATE TABLE IF NOT EXISTS Matchups (
                id   int PRIMARY KEY,
                Home varchar(255) NOT NULL,
                Away varchar(255) NOT NULL,
                Date date NOT NULL
            )
        """
        table = cur.execute(query)
        conn.commit()
        print("Processed table successfully!")
        filename.write('Processed table successfully!\n')
        return table
    except Exception as e:
        print(f"Failed to process table. Error: {e}")
        filename.write(f"Failed to process table. Error: {e}" + '\n')
        return -1
    
def clearTable(cur, conn, filename):
    try:
        query = "DELETE FROM Matchups"
        cur.execute(query)
        conn.commit()
        print("Table cleared successfully!")
        filename.write('Table cleared successfully!\n')
        return 0
    except Exception as e:
        print(f"Failed to clear table. Error: {e}")
        filename.write(f"Failed to clear table. Error: {e}" + '\n')
        return -1

def loadMatchups(data, cursor, connection, filename):
    if createTable(cursor, connection, filename) == -1:
        print("Failed to load Matchups due to invalid table.")
        filename.write('Failed to load Matchups due to invalid table.\n')
        return -1
    else:
        try:
            if (clearTable(cursor, connection, filename) == -1):
                print("Failed to load Matchups due to table not being cleared.")
                filename.write('Failed to load Matchups due to table not being cleared.\n')
                return -1
            
            insert_query = """
                INSERT INTO Matchups (id, Home, Away, Date)  VALUES (%s, %s, %s, %s) 
            """
            id = 1

            for i in data:
                insert_value = (id, i['Home'], i['Away'], i['Date'])
                cursor.execute(insert_query, insert_value)
                connection.commit()
                id += 1
                print(f'Inserted value: {insert_value}')
                filename.write(f'Inserted value: {insert_value}' + '\n')

            print('All Matchups inserted!')
            filename.write('All Matchups inserted!\n')

        except Exception as e:
            print(f"Failed to insert values into table. Error: {e}")
            filename.write(f"Failed to insert values into table. Error: {e}" + '\n')
            return -1
    