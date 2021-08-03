from MyConnection import ConnectToOracle, GetCursor

def PrintSalaryTable(connection):
	cursor = GetCursor(connection)
	SQL = "SELECT * FROM PYTHON.PHONE_TABLE"
	cursor.execute(SQL)

	for firstName, lastName, phone in cursor.fetchall():
		print("%-10s%-10s%-10s" % (firstName, lastName, phone))


if __name__ == "__main__":
	connection = ConnectToOracle()
	PrintSalaryTable(connection)

1




