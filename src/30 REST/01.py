# python -m pip install fastapi uvicorn[standard] --user

# python -m pip install fastapi --user

# https://realpython.com/fastapi-python-web-apis/#create-a-first-api

'''
What is REST?

Representational State Transfer (REST) is a software architecture that imposes conditions on how an API should work. 
REST was initially created as a guideline to manage communication on a complex network like the internet. You can 
use REST-based architecture to support high-performing and reliable communication at scale. You can easily 
implement and modify it, bringing visibility and cross-platform portability to any API system.


The Birth of REST: Roy Fielding's Dissertation

In 2000, Roy Fielding and his colleagues had one objective: Create a standard, so any server could talk to any 
other server in the world. Here's what he came up with in his doctoral dissertation:

    I had comments from well over 500 developers, many of whom were distinguished engineers with decades of 
    experience, and I had to explain everything from the most abstract notions of Web interaction to the finest 
    details of HTTP syntax. That process honed my model down to a core set of principles, properties, and 
    constraints that are now called REST.

    Uniform interface. This means we always use HTTP verbs (GET, PUT, POST, DELETE). We always use URIs as our 
    resources. And we always get an HTTP response with a status and a body.
    
    Stateless. This means each request is self-descriptive, and has enough context for the server to process that 
    message.
    
    Client-server. There has to be clear boundaries between roles of the two two systems. One server, operationally,
    has to function as the server that is being called, and the other has to function as the one making the requests.

    Cacheable. Unless denoted, a client can cache any representation. This is possible thanks to the 
    statelessness—every representation is self-descriptive.

When building APIs, you normally use these specific HTTP methods to perform a specific action.

Normally you use:

    POST: to create data.
    GET: to read data.
    PUT: to update data.
    DELETE: to delete data.

'''
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id": item_id}
