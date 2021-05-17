import cx_Oracle


def ConnectToOracle():
    connection = None
    try:
        connection = cx_Oracle.connect(
				        user="python", 
				        password="oracle", 
				        dsn="xe")
    except cx_Oracle.DatabaseError as e:
        print(e[0].context)
        raise
    return connection

def GetCursor(connection):
    cursor = cx_Oracle.Cursor(connection)
    return cursor

if __name__ == "__main__":
    connection = ConnectToOracle()
    cursor = GetCursor(connection)




