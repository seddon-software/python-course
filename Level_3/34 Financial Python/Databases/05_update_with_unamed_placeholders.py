import sqlite3 as lite
import sys

def displayTable(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Cars")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

id = 1
price = 62300 

connection = lite.connect('test.db')

with connection:
    cursor = connection.cursor()    
    cursor.execute("UPDATE Cars SET Price=? WHERE Id=?", (price, id))
    print("Number of rows updated: %d" % cursor.rowcount)
    displayTable(connection)
    