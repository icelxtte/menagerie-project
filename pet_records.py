#Programmer: Sachorra Douglas
#Step:14
#Date:11/21/2024
# Write a Python Program that displays the records loaded in the pet table as described in Section 4.2 Loading Data in a table.

import mysql.connector
from prettytable import PrettyTable

# Connect to the MySQL server and database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Leavemealone45@',
    database='menagerie'
)

# Create a cursor to interact with the database
cursor = conn.cursor()

# Query to fetch all records from the `pet` table
query = "SELECT * FROM pet"

try:
    # Execute the query
    cursor.execute(query)

    # Fetch all the records from the `pet` table
    records = cursor.fetchall()

    # Display the records
    print("Records in the 'pet' table:")
    for record in records:
        print(record)

except mysql.connector.Error as err:
    # Handle errors, such as table not existing
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
