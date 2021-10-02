from threading import Thread
from flask import Flask, render_template
import webbrowser
import wait

# This example uses 'Jinja2' templates 

app = Flask(__name__)

class Server:    
    def __init__(self, app):
        print("serving on localhost, port 5000")
        app.debug = True
        app.run(use_reloader=False)
        Server.app = app
        
    @app.route('/hello/')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)


def client():
    wait.untilServerRunning("127.0.0.1", 5000)
    print("client up and running")
    browser = webbrowser.get('firefox')
    browser.open(f'http://localhost:5000/hello')
    browser.open(f'http://localhost:5000/hello/jim')


Thread(target=client).start()


if __name__ == "__main__":
    Server(app)
