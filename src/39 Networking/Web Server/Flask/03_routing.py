from threading import Thread
from flask import Flask
import webbrowser
import wait
import time

app = Flask(__name__)

class Server:    
    def __init__(self, app):
        print("serving on localhost, port 5000")
        app.debug = True
        app.run(use_reloader=False)
        Server.app = app
        
    @app.route("/")
    def root():
        return "Index Page"
    
    @app.route('/route1')
    def page1():
        return 'This is Route 1'
    
    @app.route('/route2')
    def page2():
        return 'This is Route 2'
    
    @app.route('/user/<name>')
    def user(name):
        return f'You are user: {name}'
    
    @app.route('/sum/<int:x>/<int:y>')
    def summation(x, y):
        return f'{x} + {y} = {x+y}'

    

def client():
    wait.untilServerRunning("127.0.0.1", 5000)
    print("client up and running")
    browser = webbrowser.get('firefox')
    urls = ['http://localhost:5000/',
            'http://localhost:5000/route1',
            'http://localhost:5000/route2',
            'http://localhost:5000/user/jim',
            'http://localhost:5000/sum/625/875',
            'http://localhost:5000/']
    for url in urls:
        time.sleep(5)
        browser.open(url, new=2)


Thread(target=client).start()

if __name__ == "__main__":
    Server(app)

