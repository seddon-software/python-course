'''
Login with:
    sudo mysql -u root -p

Create user_games with password=user1_password:
    CREATE USER 'user_games'@'localhost' IDENTIFIED BY 'games_password';
Grant privileges:
    GRANT ALL PRIVILEGES ON *.* TO 'user_games'@'localhost' WITH GRANT OPTION;
Show all users:
    SELECT user FROM mysql.user;
'''

import mysql.connector

connection = mysql.connector.connect(user='games', 
                              password='xhlesley1A',
                              host='localhost',
                              database='games')


# Create a cursor object
cursor = connection.cursor()

'''
+-------+------+---------------------+------+--------+
| id    | time | date                | name | latest |
+-------+------+---------------------+------+--------+
| 41565 |   51 | 2021-12-28 20:40:08 | -    |        |
| 42099 |   52 | 2022-01-17 17:54:58 | -    |        |
| 36859 |   52 | 2021-03-25 18:28:32 | -    |        |
| 42096 |   52 | 2022-01-17 17:51:07 | -    |        |
| 44852 |   53 | 2022-12-05 16:28:15 | -    |        |
| 52680 |   53 | 2025-12-15 16:44:43 | -    |        |
| 39373 |   54 | 2021-10-19 17:48:14 | -    |        |
| 26191 |   54 | 2020-04-08 17:58:54 | -    |        |
| 24153 |   54 | 2020-02-11 17:16:43 | -    |        |
| 43740 |   54 | 2022-05-11 16:55:59 | -    |        |
+-------+------+---------------------+------+--------+
'''

try:
    cursor.execute("DROP TABLE results")
except Exception as e:
    print(e)

# SQL query to create the table
createTable = """CREATE TABLE results (
                 id INT AUTO_INCREMENT PRIMARY KEY,
                 time INT,
                 date DATE,
                 name VARCHAR(255),
                 latest VARCHAR(255)
                );"""

cursor.execute(createTable)
connection.commit()
connection.close()

