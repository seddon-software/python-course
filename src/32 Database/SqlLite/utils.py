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
