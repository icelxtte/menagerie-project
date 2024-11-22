#Programmer: Sachorra Douglas
#Step:23
#Date:11/21/2024
# Write a Python Program that returns from the pet table, how many pets each owner has.

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

# Count how many pets each owner has
cursor.execute("SELECT owner_id, COUNT(*) FROM pet GROUP BY owner_id")

# Fetch and display the results
results = cursor.fetchall()
for result in results:
    print(f"Owner ID: {result[0]}, Number of Pets: {result[1]}")

# Close the cursor and connection
cursor.close()
conn.close()
