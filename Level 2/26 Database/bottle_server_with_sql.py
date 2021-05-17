# This is a REST server
#    GET    /customer/          returns list of customers
#    GET    /customer/<name>    returns details of customer
#    DELETE /customer/<name>    deletes customer
#    POST   /customer/<name>    inserts a new customer
#    PUT    /customer/<name>    updates a customer



import sqlite3
import sqlite3 as lite
import sys

connection = lite.connect('Customers.db')

with connection:
    cursor = connection.cursor()    
    cursor.executescript("DROP TABLE IF EXISTS Customers")
    cursor.execute("CREATE TABLE Customers(Name TEXT, Age INT, City TEXT)")
    cursor.execute("INSERT INTO Customers VALUES('john',27,'London')")
    cursor.execute("INSERT INTO Customers VALUES('susan',31,'Glasgow')")
    cursor.execute("INSERT INTO Customers VALUES('istvan',44,'Paris')")
    cursor.execute("INSERT INTO Customers VALUES('joel',21,'Milan')")
    cursor.execute("INSERT INTO Customers VALUES('leo',25,'New York')")

import bottle
from bottle import route, run, request, abort, error

class Customer:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
    def getName(self):
        return self.name
    def changeAge(self, newAge):
        self.age = newAge
    def changeCity(self, newCity):
        self.city = newCity
    def details(self):
        return self.name + "," + str(self.age) + "," + self.city
    
class Customers:
    def __init__(self):
        self.mylist = {}
        
    def add(self, customer):
        key = customer.getName()
        value = customer
        self.mylist[key] = value
        
    def update(self, name, age, city):
        key = name
        value = Customer(name, age, city)
        self.mylist[key] = value
        
    def remove(self, customerName):
        key = customerName
        if key in self.mylist:
            self.mylist.pop(key)
            return True
        else:
            return False
    
    def listing(self):
        theList = []
        for c in list(self.mylist.values()):
            theList.append(c.details())
        return theList
            
    def view(self, customerName):
        key = customerName
        return self.mylist.get(key)
    
db = Customers()
def populateCustomers(db):
    with connection:
        cursor = connection.cursor()    
        cursor.execute("SELECT * FROM Customers")
        rows = cursor.fetchall()
    
        for row in rows:
            customer = Customer(row[0], row[1], row[2])
            db.add(customer)        
populateCustomers(db)

@error(404)
def not_found(error):
    e = error
    from json import dumps
    rv = {"success" : False, "result" : "unknown URL", "error" : error.body}
    return dumps(rv)

@route('/customer/', method='GET')
def recipes_list():
    return {"success" : True, "result" : db.listing() }

@route('/customer/<name>', method='GET')
def recipe_show(name):
    if name in db.mylist:
        customer = db.view(name)
        return {"success" : True, "result" : customer.details()}
    else:
        return {"success" : False}
    
@route('/customer/<name>', method='DELETE' )
def recipe_delete(name):
    if name in db.mylist:
        db.remove(name)

        try:
            with connection:
                cursor = connection.cursor()    
                cursor.execute("DELETE FROM Customers WHERE Name=?", (name,))
        except Exception as e:
            print(e)
        return {"success" : True}
    else:
        return {"success" : False}

# create
@route('/customer/<name>', method='POST')
def recipe_save(name):
    if name not in db.mylist:
        age = int(request.query.get("age"))
        city = request.query.get("city")
        db.add(Customer(name, age, city))
        with connection:
            cursor = connection.cursor()    
            cursor.execute("INSERT INTO Customers VALUES({},{},{})".format(name,age,city))
        return {"success" : True}
    else:
        return {"success" : False}

# update
@route('/customer/<name>', method='PUT')
def recipe_update(name):
    if name in db.mylist:
        age = int(request.query.get("age"))
        city = request.query.get("city")
        db.update(name, age, city)
        with connection:
            cursor = connection.cursor()    
            cursor.execute("UPDATE Customers SET AGE=?, CITY=? WHERE NAME=?", (age, city, name))
#            cursor.execute("UPDATE tasks SET col1 = ? ,col2 = ?,col3 = ?,col4 = ? WHERE colx= ? ", (v1,v2,v3,v4,vx))
        return {"success" : True}
    else:
        return {"success" : False}
   
    
bottle.debug(True) 
run(host='localhost', port=8001, debug=True)

