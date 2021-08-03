import cx_Oracle
from MyConnection import ConnectToOracle, GetCursor



def UseStoredProcedure(connection, name, increase):
    try:
        cursor = GetCursor(connection)
        newSalary = cursor.var(cx_Oracle.NUMBER)
        result = cursor.callproc('PYTHON.INCREASE_SALARY',[name, increase, newSalary])
        print("result=", result)
        print("newSalary=", newSalary)
        print("newSalary=", newSalary.getvalue())
        connection.commit()
    except Exception as reason:
        connection.rollback()
        print(type(reason))
        print("context: ", reason.message.context)
        print("code: ", reason.message.code)
        print("message: ", reason.message.message)


connection = ConnectToOracle()
print("========================================")

# this should fail
UseStoredProcedure(connection, name="Charlesx", increase=10000.0)
print("========================================")

# this should succeed
UseStoredProcedure(connection, name="Charles", increase=10000.0)
print("========================================")



