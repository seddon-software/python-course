# python -m pip install fastapi uvicorn[standard] --user

# python -m pip install fastapi --user

# https://realpython.com/fastapi-python-web-apis/#create-a-first-api

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}
