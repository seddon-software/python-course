import mysql.connector
from mysql.connector import connect, Error

def getConnection():
    return mysql.connector.connect(
        host="localhost",
        user="user1",
        password="user1"
    )

def getSQLcommands(fileName):
    f = open(fileName)
    full_sql = f.read() 
    sql_commands = full_sql.split(';') 
    sql_commands = [sql.strip() for sql in sql_commands if sql] # remove empty entries
    f.close()
    return sql_commands

def executeSQLCommands(sqlCommands):
    connection = getConnection()
    cursor = connection.cursor(buffered=True)

    for sql in sqlCommands: 
        try:
            print(sql)
            cursor.execute(sql)
        except Error as e:
            print(f"*** Error: {e}")
            cursor = connection.cursor(buffered=True)
    cursor.close() 
    connection.close()

phonesSQL = getSQLcommands("SQL/CreatePhonesTable.sql")
executeSQLCommands(phonesSQL)
salariesSQL = getSQLcommands("SQL/CreateSalaryTable.sql")
executeSQLCommands(salariesSQL)
