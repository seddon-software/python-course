from threading import Thread
from flask import Flask, request
import webbrowser
import wait  # this module is local


def client():
    wait.untilServerRunning("127.0.0.1", 5000)
    print("client up and running")
    browser = webbrowser.get('firefox')
    #browser.open(f'http://localhost:5000/')
    browser.open(f'http://localhost:5000/sum?x=25&y=40')

Thread(target=client).start()

app = Flask(__name__)

class Server:    
    def __init__(self, app):
        print("serving on localhost, port 5000")
        app.debug = True
        app.run(use_reloader=False)
        Server.app = app
        
    @app.route("/")
    def root():
        return "Hello World"

    @app.route("/sum")
    def add():
        x = request.args.get('x')
        y = request.args.get('y')
        return f"{x} + {y} = {int(x) + int(y)}" 

if __name__ == "__main__":
    Server(app)
    
