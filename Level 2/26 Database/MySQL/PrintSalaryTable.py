from MyConnection import ConnectToOracle, GetCursor

def PrintSalaryTable(connection):
	cursor = GetCursor(connection)
	SQL = "SELECT * FROM PYTHON.SALARY_TABLE"
	cursor.execute(SQL)

	for name, salary in cursor.fetchall():
		print("%-10s%-10i" % (name, salary))


if __name__ == "__main__":
	connection = ConnectToOracle()
	PrintSalaryTable(connection)

1




