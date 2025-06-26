"""
Write a Python program to connect to an SQLite3 database, create a table, insert data, and 
fetch data. 
"""

import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER,
                    department TEXT
                )''')

cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)",
               ('Alice', 30, 'HR'))
cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)",
               ('Bob', 25, 'Engineering'))
cursor.execute("INSERT INTO employees (name, age, department) VALUES (?, ?, ?)",
               ('Charlie', 28, 'Marketing'))

connection.commit()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

print("Employee Records:")
for row in rows:
    print(row)

connection.close()