import cx_Oracle
from MyConnection import ConnectToOracle, GetCursor
from PrintSalaryTable import PrintSalaryTable


def DeleteRow(connection, name):
    try:
        SQL = "DELETE FROM PYTHON.SALARY_TABLE WHERE Name = '" + name + "'"
        cursor = GetCursor(connection)
        cursor.execute(SQL)
        connection.commit()
    except Exception as reason:
        print(reason)
        connection.rollback()

if __name__ == "__main__":
	connection = ConnectToOracle()
	DeleteRow(connection, "George")


1



