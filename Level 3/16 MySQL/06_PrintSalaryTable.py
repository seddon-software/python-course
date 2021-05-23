from utils import *

connection = getConnection()

cursor = getCursor(connection, "PYTHON.SALARY_TABLE")
for name, salary in cursor.fetchall():
    print(f"{name:<10s}{salary:<10.0f}")






