from utils import *

connection = getConnection("database.db")

cursor = getCursor(connection, "SALARY_TABLE")
for name, salary in cursor.fetchall():
    print(f"{name:<10s}{salary:<10.0f}")






