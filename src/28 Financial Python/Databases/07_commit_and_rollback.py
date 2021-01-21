import sqlite3 as lite
import sys


def displayTable(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Cars")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

try:
    connection = lite.connect('test.db')
    cursor = connection.cursor()
    cursor.executescript("""
        DROP TABLE IF EXISTS Cars;
        CREATE TABLE Cars(Id INT, Name TEXT, Price INT);
        INSERT INTO Cars VALUES(1,'Audi',52642);
        INSERT INTO Cars VALUES(2,'Mercedes',57127);
        INSERT INTO Cars VALUES(3,'Skoda',9000);
        INSERT INTO Cars VALUES(4,'Volvo',29000);
        INSERT INTO Cars VALUES(5,'Bentley',350000);
        INSERT INTO Cars VALUES(6,'Citroen',21000);
        INSERT INTO Cars VALUES(7,'Hummer',41400);
        INSERT INTO Cars VALUES(8,'Volkswagen',21600);
        """)
    connection.commit()
    displayTable(connection)
    cursor.executescript("INSERT INTO Cars VALUES(AAAA,'Morgan',19000);");
except lite.Error as e:
    if connection:
        connection.rollback()
    print("Error {}:".format(e))
    sys.exit(1)
finally:

    if connection:
        connection.close() 
        
        