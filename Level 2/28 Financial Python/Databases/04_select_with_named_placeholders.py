import sqlite3 as lite
import sys

def displayTable(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Cars")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

id = 4
connection = lite.connect('test.db')
with connection:
    cur = connection.cursor()    
    cur.execute("SELECT Name, Price FROM Cars WHERE Id=:Id", {"Id": id})    
    row = cur.fetchone()
    print(row[0], row[1])
    displayTable(connection)
    