from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'This is the FLASK app index page'

@app.route('/view1')
def view1():
   return 'This is view 1'

@app.route('/view2')
def view2():
   return 'This is view 2'

# routes with parameters
@app.route('/week/<int:n>')
def week(n):
   return f'This is week {n}'

@app.route('/convert/<float:t>')
def centigrade(t):
   return f'{t} C = {t*1.8 + 32} F'
from flask import render_template
@app.route('/template')
def template():
    cities = ["London", "New York", "Rome", "Paris", "Tokyo"]
    salaries = [{"Peter":22000, "Ali":41000, "Suzi":42000, "Henry":31000, "Khalid":27500}]
    return render_template("mytemplate.html", param1=cities, param2=salaries) 
