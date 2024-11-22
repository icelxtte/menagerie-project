#Programmer: Sachorra Douglas
#Step:7
#Date:11/21/2024

import mysql.connector

# Establish connection to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Leavemealone45@'
)

# Create a cursor to interact with MySQL
cursor = conn.cursor(buffered=True)  # Use a buffered cursor to avoid unread results

try:
    # Show all databases
    cursor.execute("SHOW DATABASES")

    # Fetch the results to clear the query result state
    databases = cursor.fetchall()
    print("Databases:", databases)

    # Drop the menagerie database if it exists
    cursor.execute("DROP DATABASE IF EXISTS menagerie")
    print("Database 'menagerie' dropped if it existed.")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
