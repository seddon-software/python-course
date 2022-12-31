import sqlite3
from sqlite3 import Error


def getConnection(db_file):
    """ create a database connection to a SQLite database """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return connection

def getCursor(connection, table):
    cursor = connection.cursor()
    SQL = f"SELECT * FROM {table}"
    cursor.execute(SQL)
    return cursor

def setup_database(db_file):
    """ create a database connection to a SQLite database """
    connection = getConnection(db_file)
    print(sqlite3.version)
    cursor = connection.cursor()
    cursor.executescript("DROP TABLE IF EXISTS Customers")
    cursor.execute("CREATE TABLE Customers(Name TEXT UNIQUE, Age INT, City TEXT);")
    cursor = getCursor(connection, "Customers")    
    SQL='''INSERT INTO Customers (Name, Age, City) VALUES('john',27,'London');
           INSERT INTO Customers (Name, Age, City) VALUES('susan',31,'Glasgow');
           INSERT INTO Customers (Name, Age, City) VALUES('istvan',44,'Paris');
           INSERT INTO Customers (Name, Age, City) VALUES('joel',21,'Milan');
           INSERT INTO Customers (Name, Age, City) VALUES('leo',25,'New York');
        '''
    cursor.executescript(SQL)
    cursor.close()
    connection.close()

if __name__ == '__main__':
    setup_database("Customers.db")

    connection = getConnection("Customers.db")
    cursor = getCursor(connection, "Customers")    
    for firstName, lastName, phone in cursor.fetchall():
        print(f"{firstName:<10s}{lastName:<10}{phone:<10s}")

