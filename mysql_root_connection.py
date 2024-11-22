#Programmer: Sachorra Douglas
#Step:2
#Date:11/21/2024

import mysql.connector

try:
    # Establish connection to MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Leavemealone45@'
    )
    print("Connection successful!")

    # Create a cursor to interact with MySQL
    cursor = conn.cursor()

    # Close the cursor and connection
    cursor.close()
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")
