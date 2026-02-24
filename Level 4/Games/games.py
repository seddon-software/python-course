'''
This is the Memory game.  This is the server (written using Flask).

To run the client use:
    http://localhost:5000/memory6

Results are stored in MySql server.

The database 'games' holds records in table 'results' that look like:

    +------+---------------------+------+--------+
    | time | date                | name | latest |
    +------+---------------------+------+--------+
    |   51 | 2021-12-28 20:40:08 | -    |        |
    |   52 | 2022-01-17 17:54:58 | -    |        |
    |   52 | 2021-03-25 18:28:32 | -    |        |
    |   52 | 2022-01-17 17:51:07 | -    |        |
    |   53 | 2022-12-05 16:28:15 | -    |        |
    |   53 | 2025-12-15 16:44:43 | -    |        |
    |   54 | 2021-10-19 17:48:14 | -    |        |
    |   54 | 2020-04-08 17:58:54 | -    |        |
    |   54 | 2020-02-11 17:16:43 | -    |        |
    |   54 | 2022-05-11 16:55:59 | -    |    *   |
    +------+---------------------+------+--------+

these need to be returned to the client in the form:

    topTenResults = 
       ["51 2021-12-28 20:40:08", 
        "52 2022-01-17 17:54:58", 
        "52 2021-03-25 18:28:32", 
        "52 2022-01-17 17:51:07",
        "53 2022-12-05 16:28:15", 
        "53 2025-12-15 16:44:43",
        "54 2021-10-19 17:48:14", 
        "54 2020-04-08 17:58:54", 
        "54 2020-02-11 17:16:43",
        "54 2022-05-11 16:55:59"]

As you can see by inspection of 'connectToMySql()' we login to MySql server with account=games.
'''

debug = True

from flask import Flask
from flask import render_template, send_file, request, jsonify, logging
#import mysql.connector
import sqlite3
from datetime import datetime
from urllib.parse import parse_qs
import logging

def connectToDatabase():
    connection = sqlite3.connect("games.db")
    return connection

def createTable():
    connection = sqlite3.connect("games.db")
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE TABLE results(time, date, name, latest)")
    except Exception as e:
        if debug: print(e)

createTable()       # does nothing if games.db exists

def test1():
    connection = sqlite3.connect("games.db")
    cursor = connection.cursor()
    res = cursor.execute("SELECT * FROM results")
    print(res.fetchone())
    connection = sqlite3.connect("games.db-")
    cursor = connection.cursor()
    res = cursor.execute("SELECT * FROM results")
    print(res.fetchone())

test1()

def clearLatestResultFlag(name):
    connection = connectToDatabase()
    cursor = connection.cursor()
    sql = f"UPDATE results SET latest = ' ' WHERE name = '{name}'"
    cursor.execute(sql)
    connection.commit()
    connection.close()

def updateDatabaseWithLatestResult(time, name):
    connection = connectToDatabase()
    try:
        clearLatestResultFlag(name)
    except Exception as e:
        print(e)
    cursor = connection.cursor()
    current_date = datetime.now()
    date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    latest = '*'
    try:
        sql = f"INSERT INTO results (time, date, name, latest) VALUES ({time}, '{date}', '{name}', '{latest}');"
        cursor.execute(sql)
    except Exception as e:
        print(e)
        print(sql)
    connection.commit()
    connection.close()

def displayTable():
    connection = connectToDatabase()
    cursor = connection.cursor()
    sql = f"SELECT time, date, latest FROM results;"
    cursor.execute(sql)
    results = cursor.fetchall() # returns a list of 10 tuples

def getTopTenResultsFromDatabase(name):
    connection = connectToDatabase()
    cursor = connection.cursor()
    sql = f"SELECT time, date, latest FROM results WHERE name = '{name}' ORDER BY time ASC, date DESC LIMIT 10;"
    cursor.execute(sql)
    results = cursor.fetchall() # returns a list of 10 tuples
    
    topTenResults = []

    for result in results:
        time = result[0]
        date = result[1]   #.strftime("%Y-%m-%d")
        latest = result[2]
        if latest == "*": 
            date = date + "*"     # browser will highlight this record in red
        topTenResults.append(f"{time} {date}")
    displayTable()
    return topTenResults

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app.logger.setLevel(logging.DEBUG)

def processAjaxCallback(time, name):
    if time > 0:
        updateDatabaseWithLatestResult(time, name)
        topTenResults = getTopTenResultsFromDatabase(name)
    return topTenResults

@app.route("/memory6")
def hello():
    return render_template('memory6.html')

@app.route('/css/<path:filename>')
def base_static(filename):
    return send_file(f"css/{filename}")

@app.route('/jquery/<path:filename>')
def base_static2(filename):
    return send_file(f"jquery/{filename}")

@app.route('/images/cards/<path:filename>')
def base_static3(filename):
    return send_file(f'images/cards/{filename}')


# Ajax callback
@app.route('/games/MemoryServer')
def results():
    queryString = request.query_string

    json = parse_qs(queryString.decode())
    time = int(json['time'][0])
    name = json['name'][0]
    data = processAjaxCallback(time, name)
    return jsonify(data)
    
# run the application
if __name__ == "__main__":
    app.run(debug=True, port=5001)
