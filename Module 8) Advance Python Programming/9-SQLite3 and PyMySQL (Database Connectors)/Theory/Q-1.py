"""
 Introduction to SQLite3 and PyMySQL for database connectivity. 

 -->  Theoretical Overview of SQLite3 and PyMySQL

SQLite3 and PyMySQL are two popular tools for working with databases in Python. Both are used to manage, query, and manipulate data but are suited for different types of applications.


 1. SQLite3
SQLite3 is a lightweight, self-contained, serverless relational database management system (RDBMS) that is built into Python.

# Key Features:
- No Server Required: SQLite3 is serverless, meaning it operates directly from the file system. It uses `.sqlite` or `.db` files to store data.
- Built into Python: The `sqlite3` module is part of Python's standard library, so no external installation is needed.
- Lightweight: Ideal for small- to medium-scale applications or for prototyping.

# Advantages:
- Easy to use and set up.
- No need for an external database server.
- Suitable for embedded systems, mobile devices, and small web apps.

# Example Use Case:
SQLite3 is commonly used for storing lightweight data, such as user preferences in desktop apps or data for small-scale web applications.


 Basic Steps to Use SQLite3 in Python:
1. Import the Module:
   ```
   import sqlite3
   ```

2. Connect to the Database:
   - If the database file doesn't exist, it will create one.
   ```
   connection = sqlite3.connect("example.db")
   ```

3. Create a Cursor Object:
   - The cursor is used to execute SQL commands.
   ```
   cursor = connection.cursor()
   ```

4. Execute SQL Statements:
   - Use SQL commands like `CREATE TABLE`, `INSERT`, `SELECT`.
   ```
   cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
   ```

5. Commit Changes and Close:
   ```python
   connection.commit()
   connection.close()
   ```


 2. PyMySQL
PyMySQL is a Python library used to connect to MySQL databases. Unlike SQLite3, MySQL is a server-based RDBMS, making it suitable for large-scale, multi-user applications.

# Key Features:
- MySQL Connectivity: Allows Python to communicate with remote or local MySQL servers.
- Supports Authentication: Handles user credentials, permissions, and database security.
- Scalable: Designed for large, multi-user, distributed systems.

# Advantages:
- Ideal for web applications with high concurrency needs.
- Compatible with cloud databases and remote servers.
- Offers robust support for transactions and advanced SQL features.

# Example Use Case:
PyMySQL is widely used for database-driven websites and applications, such as e-commerce platforms or data-intensive services.


 Basic Steps to Use PyMySQL in Python:
1. Install the Library:
   - PyMySQL is not built into Python, so it must be installed separately.
   ```bash
   pip install pymysql
   ```

2. Import the Module:
   ```
   import pymysql
   ```

3. Connect to the MySQL Server:
   - Requires server details like host, username, and password.
   ```
   connection = pymysql.connect(
       host="localhost",
       user="root",
       password="password",
       database="example_db"
   )
   ```

4. Create a Cursor Object:
   ```
   cursor = connection.cursor()
   ```

5. Execute SQL Statements:
   ```
   cursor.execute("SELECT * FROM users")
   for row in cursor.fetchall():
       print(row)
   ```

6. Commit Changes and Close:
   ```
   connection.commit()
   connection.close()
   ```


 Comparison Between SQLite3 and PyMySQL

| Feature          | SQLite3                        | PyMySQL                         |
|------------------|------------------------------------|--------------------------------------|
| Type         | Serverless (embedded RDBMS)        | Server-based (requires MySQL server)|
| Setup        | No external setup (built-in)       | Requires MySQL server and library   |
| Scalability  | Suitable for small-scale apps      | Suitable for large-scale, multi-user apps |
| Speed        | Faster for local data access       | Optimized for distributed systems   |
| Example Use  | Lightweight apps or local storage  | Web apps, large-scale systems       |


 Conclusion
Both SQLite3 and PyMySQL offer efficient database connectivity for Python, but their use depends on the application's requirements. SQLite3 is ideal for small, serverless applications, while PyMySQL is better suited for scalable, server-based solutions with complex requirements. Their seamless integration with Python makes database management simple and effective.
"""