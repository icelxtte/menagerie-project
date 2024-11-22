#Programmer: Sachorra Douglas
#Step:10
#Date:11/21/2024
# Write a Python Program that shows the structure of the pet table.

import mysql.connector
from prettytable import PrettyTable #creates the table

# Step 1: Connect to MySQL server and ensure the database exists
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Leavemealone45@'
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS menagerie")
cursor.close()
conn.close()

# Step 2: Connect to the `menagerie` database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Leavemealone45@',
    database='menagerie'
)

cursor = conn.cursor()

# Step 3: Create the `pet` table
create_table_query = """
CREATE TABLE IF NOT EXISTS pet (
    name VARCHAR(20),
    birth DATE,
    month_of_birth INT
)
"""
cursor.execute(create_table_query)

# Step 4: Insert data into the `pet` table
insert_data_query = """
INSERT INTO pet (name, birth, month_of_birth)
VALUES 
    ('Fluffy', '1993-02-04', 2),
    ('Claws', '1994-03-17', 3),
    ('Buffy', '1989-05-13', 5),
    ('Fang', '1990-08-27', 8),
    ('Bowser', '1989-08-31', 8),
    ('Chirpy', '1998-09-11', 9),
    ('Whistler', '1997-12-09', 12),
    ('Slim', '1996-04-29', 4),
    ('Puffball', '1999-03-30', 3)
ON DUPLICATE KEY UPDATE
    name = VALUES(name)
"""
cursor.execute(insert_data_query)

# Commit the changes
conn.commit()

# Step 5: Fetch and display table data in tabular format
cursor.execute("SELECT * FROM pet")
rows = cursor.fetchall()

# Use PrettyTable to format the output
table = PrettyTable()
table.field_names = ["Name", "Birth", "Month (Birth)"]

for row in rows:
    table.add_row(row)

print("Contents of the 'pet' table:")
print(table)

# Close the cursor and connection
cursor.close()
conn.close()
