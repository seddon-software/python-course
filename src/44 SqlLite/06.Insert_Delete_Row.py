from utils import getConnection, getCursor

def insertRow(connection, name, salary):
    table = "SALARY_TABLE"
    cursor = getCursor(connection, table)
    try:
        SQL = f"INSERT INTO {table} (Name, Salary) " + \
		      f"VALUES ('{name}', '{salary}')"
        print(SQL)
        cursor.execute(SQL)
        connection.commit()
    except Exception as reason:
        connection.rollback()
        print(reason)


def deleteRow(connection, name):
    table = "SALARY_TABLE"
    try:
        SQL = f"DELETE FROM {table} WHERE Name = '{name}'"
        print(SQL)
#        cursor = connection.cursor(buffered=True)
        cursor = connection.cursor()
        cursor.execute(SQL)
        connection.commit()
    except Exception as reason:
        print(reason)
        connection.rollback()

def printTable(connection):
	cursor = getCursor(connection, "SALARY_TABLE")
	for name, salary in cursor.fetchall():
	    print(f"{name:<10s}{salary:<10.0f}")

if __name__ == "__main__":
    connection = getConnection("database.db")
    printTable(connection)
    insertRow(connection, "George", 15000.0)
    printTable(connection)
	# clean up
    deleteRow(connection, "George")
    printTable(connection)
		
