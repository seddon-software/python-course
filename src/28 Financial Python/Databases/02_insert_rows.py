import sqlite3 as lite
import sys

connection = lite.connect('test.db')

with connection:
    cursor = connection.cursor()    
    cursor.executescript("DROP TABLE IF EXISTS Cars")
    cursor.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
    cursor.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
    cursor.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
    cursor.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
    cursor.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
    cursor.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
    cursor.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
    cursor.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
    cursor.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
    
