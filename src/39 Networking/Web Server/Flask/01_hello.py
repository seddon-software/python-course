from threading import Thread
from flask import Flask
import webbrowser
import wait


def client():
    wait.untilServerRunning("127.0.0.1", 5000)
    print("client up and running")
    browser = webbrowser.get('firefox')
    browser.open(f'http://localhost:5000/')

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
        return "hello"


if __name__ == "__main__":
    Server(app)
    
