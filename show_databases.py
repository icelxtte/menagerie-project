#Programmer: Sachorra Douglas
#Step:4
#Date:11/21/2024

import mysql.connector

# Correct password
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Leavemealone45@'
)

cursor = conn.cursor()
cursor.execute("SHOW DATABASES")

# Fetch and display all databases
databases = cursor.fetchall()
for database in databases:
    print(database[0])

cursor.close()
conn.close()
