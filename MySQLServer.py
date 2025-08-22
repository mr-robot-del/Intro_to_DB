import sys
import mysql.connector
from mysql.connector import Error

if len(sys.argv) != 3:
    print("Usage: python MySQLServer.py <username> <password>")
    sys.exit(1)

username = sys.argv[1]
password = sys.argv[2]

conn = None
cursor = None

try:
    conn = mysql.connector.connect(
        host="localhost",
        user=username,
        password=password
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except Error as e:
    if e.errno == 1007:
        pass  # Database already exists, do not fail
    else:
        print(f"Error: {e}")
finally:
    if cursor is not None:
        cursor.close()
    if conn is not None and conn.is_connected():
        conn.close()
