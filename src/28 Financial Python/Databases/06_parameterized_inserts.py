import sqlite3 as lite
import sys


def displayTable(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Cars")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
    (4, 'Volvo', 29000),
    (5, 'Bentley', 350000),
    (6, 'Hummer', 41400),
    (7, 'Volkswagen', 21600)
)


connection = lite.connect('test.db')

with connection:    
    current = connection.cursor()    
    current.execute("DROP TABLE IF EXISTS Cars")
    current.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    current.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
    displayTable(connection)
