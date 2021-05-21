import cx_Oracle
from MyConnection import ConnectToOracle, GetCursor
from PrintSalaryTable import PrintSalaryTable
from DeleteRow import DeleteRow


def InsertRow(connection, name, salary):
	try:
		SQL = "INSERT INTO PYTHON.SALARY_TABLE (Name, Salary) " + \
		      "VALUES ('" + name   +"'" + \
		      "       ,'" + str(salary) +"')"
		cursor = GetCursor(connection)
		cursor.execute(SQL)
		cursor.close()
		connection.commit()
	except Exception as reason:
		connection.rollback()
		print(reason)


connection = ConnectToOracle()
InsertRow(connection, "George", 15000.0)
PrintSalaryTable(connection)
DeleteRow(connection, "George")
PrintSalaryTable(connection )

