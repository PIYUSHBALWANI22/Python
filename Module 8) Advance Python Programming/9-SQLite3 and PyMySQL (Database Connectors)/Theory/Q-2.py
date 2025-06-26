"""
Creating and executing SQL queries from Python using these connectors.

--> Creating and executing SQL queries from Python using SQLite3 or PyMySQL involves establishing a connection between Python and the database, using SQL commands to interact with the database, and managing the results. Here's a theoretical explanation with examples for both SQLite3 and PyMySQL:


 1. Using SQLite3 to Execute SQL Queries

SQLite3 is an embedded database system, so it doesn't require a server. Here's how to create and execute SQL queries using the `sqlite3` module in Python:

# Steps:
1. Connect to the Database:
   - Use `sqlite3.connect()` to connect to an existing database or create a new one.

2. Create a Cursor Object:
   - Use the `cursor()` method to obtain a cursor object to execute SQL queries.

3. Execute SQL Queries:
   - Use the `execute()` method of the cursor object to run SQL commands like `CREATE`, `INSERT`, `SELECT`, etc.

4. Commit Changes:
   - Use the `commit()` method of the connection object to save any modifications (e.g., `INSERT`, `UPDATE`).

5. Fetch Results:
   - Use methods like `fetchone()`, `fetchall()`, or `fetchmany()` to retrieve query results.

6. Close the Connection:
   - Always close the connection using `close()`.

# Example:
```
import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("example.db")
cursor = connection.cursor()

# Create a table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# Commit changes
connection.commit()

# Retrieve data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()
```


 2. Using PyMySQL to Execute SQL Queries

PyMySQL is a library used for connecting to MySQL databases. Here's how to create and execute SQL queries using the `pymysql` module in Python:

# Steps:
1. Install PyMySQL:
   - Install the module using `pip install pymysql`.

2. Connect to the MySQL Server:
   - Use `pymysql.connect()` with credentials like host, user, password, and database.

3. Create a Cursor Object:
   - Obtain a cursor object using the `cursor()` method to execute SQL commands.

4. Execute SQL Queries:
   - Run SQL queries using the `execute()` method of the cursor.

5. Commit Changes:
   - Save modifications to the database with the `commit()` method.

6. Fetch Results:
   - Retrieve data using methods like `fetchone()`, `fetchall()`, etc.

7. Close the Connection:
   - Close the connection using `close()` to release resources.

# Example:
```
import pymysql

# Connect to MySQL database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="password",
    database="example_db"
)
cursor = connection.cursor()

# Create a table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), age INT)")

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# Commit changes
connection.commit()

# Retrieve data
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
connection.close()
```


 Comparison of SQLite3 and PyMySQL for Query Execution

| Aspect             | SQLite3                         | PyMySQL                          |
|------------------------|-------------------------------------|--------------------------------------|
| Setup              | No additional installation needed   | Requires MySQL server and PyMySQL installation |
| Connection         | Directly connects to `.db` file     | Connects to a MySQL server          |
| Use Case           | Lightweight, embedded applications  | Scalable, server-based applications |
| Concurrency        | Limited concurrency support         | Handles multiple users and connections |


 Conclusion
The process of creating and executing SQL queries using SQLite3 and PyMySQL in Python follows similar steps but caters to different use cases. SQLite3 is ideal for lightweight, serverless applications, while PyMySQL is better suited for large-scale, server-based systems. These connectors enable Python developers to work seamlessly with relational databases in various environments.
"""