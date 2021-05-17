import sqlite3 as lite
import sys

connection = lite.connect('test.db')

with connection:
    cursor = connection.cursor()    
    cursor.execute("SELECT * FROM Cars")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    print()
    
    print("{:2s}{:>12s}{:>8s}".format("ID", "Maker", "Cost"))
    print("{:2s}{:>12s}{:>8s}".format("==", "=====", "===="))
    for row in rows:
        print("{:2d}{:>12s}{:8d}".format(row[0], row[1], row[2]))