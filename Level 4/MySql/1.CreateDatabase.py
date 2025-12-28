import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user1",
  password="password"
)

cursor = mydb.cursor()

try:
    cursor.execute("DROP DATABASE games")
except Exception as e:
    print(e)
cursor.execute("CREATE DATABASE games")