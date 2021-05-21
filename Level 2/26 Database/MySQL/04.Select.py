import mysql.connector
from mysql.connector import connect, Error

def getConnection():
    return mysql.connector.connect(
        host="localhost",
        user="user1",
        password="user1"
    )

def getCursor(connection, table):
    cursor = connection.cursor(buffered=True)
    SQL = f"SELECT * FROM {table}"
    cursor.execute(SQL)
    return cursor

if __name__ == "__main__":
    connection = getConnection()

    cursor = getCursor(connection, "PYTHON.PHONE_TABLE")    
    for firstName, lastName, phone in cursor.fetchall():
        print(f"{firstName:<10s}{lastName:<10s}{phone:<10s}")

    cursor = getCursor(connection, "PYTHON.SALARY_TABLE")
    for name, salary in cursor.fetchall():
        print(f"{name:<10s}{salary:<10.0f}")






