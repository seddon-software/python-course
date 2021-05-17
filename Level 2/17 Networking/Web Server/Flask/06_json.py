from threading import Thread
from flask import Flask, render_template, request
import webbrowser
import wait

from flask import jsonify
from random import randrange
from flask import json


app = Flask(__name__)

class Server:    
    def start(app):
        print("serving on localhost, port 5000")
        app.debug = True
        app.run(use_reloader=False)

    def gen():
        while True:
            n = randrange(2, 11)
            if n !=5 and n !=10: yield n

    @app.route('/')
    def begin():
        return render_template('tables.html')
    
    @app.route('/answer')
    def answer():
        try:
            result = int(request.args.get('result'))
            n1 = int(request.args.get('n1'))
            n2 = int(request.args.get('n2'))
            if n1*n2 == result:
                message = "correct"
            else:
                message = "wrong"
        except:
            message = "?"
            
        data = {'n1':next(Server.g), 'n2':next(Server.g), 'message':message}
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
        
    @app.route('/question')
    def question():
        data = {'n1':next(Server.g), 'n2':next(Server.g), 'message':''}
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response

    g = gen()   # start the generator

def client():
    wait.untilServerRunning("127.0.0.1", 5000)
    print("client up and running")
    browser = webbrowser.get('firefox')
    browser.open(f'http://localhost:5000/')

Thread(target=client).start()

if __name__ == "__main__":
    Server.start(app)
