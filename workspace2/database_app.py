from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)
class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))  
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr,pin):
       self.name = name
       self.city = city
       self.addr = addr
       self.pin = pin

db.create_all()

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
