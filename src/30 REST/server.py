#    GET    /customer/          returns list of customers
#    GET    /customer/<name>    returns details of customer
#    DELETE /customer/<name>    deletes customer
#    POST   /customer/<name>    inserts a new customer
#    PUT    /customer/<name>    updates a customer

from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from databases import Database



database = Database("sqlite+aiosqlite:///Customers.db")

app = FastAPI()

@app.on_event("startup")
async def database_connect():
    await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()

#    POST   /customer/<name>    inserts a new customer
@app.post("/customer/{name}")
async def post_data(name:str, age:int, city:str):
    sql = f"INSERT INTO Customers(name, age, city) VALUES('{name}', '{age}', '{city}');"
    try:
        await database.execute(sql)
        return "OK"
    except Exception as e:
        print(f"**** {e}")
        raise HTTPException(status_code=404, detail=f"{e} {name}")

#    GET    /customer/          returns list of customers
@app.get("/customer")
async def get_data():
    query = f"SELECT * FROM Customers"
    results = await database.fetch_all(query=query)
    return results

#    GET    /customer/<name>    returns details of customer
@app.get("/customer/{name}")
async def get_data(name: str):
    query = f"SELECT * FROM Customers WHERE Name = '{name}'"
    results = await database.fetch_all(query=query)
    return results

#    PUT    /customer/<name>    updates a customer
@app.put("/customer/{name}")
async def put_data(name:str, age:int, city:str):
    sql = f"UPDATE Customers SET age={age}, city='{city}' WHERE NAME='{name}'" 
    await database.execute(sql)

#    DELETE /customer/<name>    deletes customer
@app.delete("/customer/{name}")
async def delete_data(name:str):
    sql = f"DELETE from Customers WHERE NAME='{name}'" 
    try:
        await database.execute(sql)
        return f"{name} deleted"
    except Exception as e:
        print(f"**** {e}")
        raise HTTPException(status_code=404, detail=f"{e} {name}")
