#Programmer: Sachorra Douglas
#Step:20
#Date:11/21/2024
#Write a Python program that returns the name and birth columns from the pet table.

import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Leavemealone45@',
    database='menagerie'
)

# Create a cursor to interact with MySQL
cursor = conn.cursor()

# Fetch name and birth columns from the pet table
cursor.execute("SELECT name, birth FROM pet")

# Fetch and display the results
results = cursor.fetchall()
for result in results:
    print(result)

# Close the cursor and connection
cursor.close()
conn.close()

