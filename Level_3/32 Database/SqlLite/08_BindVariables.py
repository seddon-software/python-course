from utils import *

# benefits of bind variables:
# 1) avoid SQL injection attacks
# 2) optimize query plan

def useBindVariablesToUpdate(connection, name, salary):
    try:
        cursor = connection.cursor(prepared=True)
        SQL = 'UPDATE PYTHON.SALARY_TABLE SET salary=? WHERE name=?'
        cursor.execute(SQL, (salary, name))                            
        connection.commit()
    except Exception as reason:
        connection.rollback()
        print(reason)
	
if __name__ == "__main__":
    connection = getConnection()
    useBindVariablesToUpdate(connection, "Charles", 10005.0)

# check the update
cursor = getCursor(connection, "PYTHON.SALARY_TABLE")
for name, salary in cursor.fetchall():
    print(f"{name:<10s}{salary:<10.0f}")
