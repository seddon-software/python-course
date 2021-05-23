import mysql.connector

from mysql.connector import connect, Error

mydb = mysql.connector.connect(
    host="localhost",
    user="user1",
    password="user1"
)

# sys admin needs to issue the following:
# GRANT ALL PRIVILEGES ON `PYTHON`.* TO 'user1'@'localhost';

print(mydb) 
mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE PYTHON")
except Error as e:
    print(e)

