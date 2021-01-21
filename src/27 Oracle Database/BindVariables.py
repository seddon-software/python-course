import cx_Oracle
from MyConnection import ConnectToOracle, GetCursor
from PrintSalaryTable import PrintSalaryTable


def method1(cursor, name, salary):
        named_params = { 'aName':name, 'aSalary':salary }
        SQL = 'UPDATE PYTHON.SALARY_TABLE SET salary=:aSalary WHERE name=:aName'
        cursor.execute(SQL, named_params)
        print(cursor.bindnames())

def method2(cursor, name, salary):
        SQL = 'UPDATE PYTHON.SALARY_TABLE SET salary=:aSalary WHERE name=:aName'
        cursor.execute(SQL, aName=name, aSalary=salary )
        print(cursor.bindnames())
        
def method3(cursor, name, salary):
        SQL = 'UPDATE PYTHON.SALARY_TABLE SET salary=:1 WHERE name=:2'
        cursor.execute(SQL, (salary, name) )
        print(cursor.bindnames())

def UseBindVariables(connection, name, salary):
    try:
        cursor = GetCursor(connection)
        method1(cursor, name, salary)
        method2(cursor, name, salary)
        method3(cursor, name, salary)
        connection.commit()
    except Exception as reason:
	    connection.rollback()
	    print(reason)
	

connection = ConnectToOracle()
UseBindVariables(connection, "Charles", 10005.0)


