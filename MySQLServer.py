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
    conn.get_warnings = True
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    warnings = cursor.fetchwarnings()
    if warnings is None or len(warnings) == 0:
        print("Database 'alx_book_store' created successfully!")
except Error as e:
    print(f"Error: {e}")
finally:
    if cursor is not None:
        cursor.close()
    if conn is not None and conn.is_connected():
        conn.close()
