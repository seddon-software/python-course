from utils import *

connection = getConnection()

cursor = getCursor(connection, "PYTHON.PHONE_TABLE")    
for firstName, lastName, phone in cursor.fetchall():
    print(f"{firstName:<10s}{lastName:<10s}{phone:<10s}")






