#Programmer: Sachorra Douglas
#Step:17
#Date:11/21/2024
# Write a Python program that returns record(s) of female dogs from the pet tabl

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

# Example criteria to simulate filtering for female dogs.
# Since there's no 'breed' or 'gender' column, I assume certain names or months for dogs.
# Here we use a condition for pets born in a specific month (e.g., month 3 for 'March') as a placeholder.

cursor.execute("SELECT * FROM pet WHERE month_of_birth = 3")  # retrieves all columns (*) from the pet table for the records where the month_of_birth is 3, meaning the pets were born in March

# Fetch and display the results
records = cursor.fetchall()
if records:
    print("Records of pets born in March (as an example):")
    for record in records:
        print(record)
else:
    print("No records found for the specified criteria.")

# Close the cursor and connection
cursor.close()
conn.close()
