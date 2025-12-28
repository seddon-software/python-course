import mysql.connector
from datetime import time, date, datetime

connection = mysql.connector.connect(
    user='games',
    password='xhlesley1A',
    host='localhost',
    database='games')


# Create a cursor object
cursor = connection.cursor()

now = datetime(2009,5,5)

sql = f"INSERT INTO results (time, date, name, latest) VALUES (125, '{now}', 'John', '*')"

try:
    cursor.execute(sql)
except Exception as e:
    print(e)
connection.commit()
connection.close()

