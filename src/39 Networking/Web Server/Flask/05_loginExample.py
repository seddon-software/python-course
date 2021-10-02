from threading import Thread
from flask import Flask, render_template, request
import webbrowser
import wait
import time


app = Flask(__name__)
class Server:
    loginTable = { 
                   'tom' : 'mot',
                   'sue' : 'eus',
                   'jim' : 'mij'
                  }
    
    def start(app):
        print("serving on localhost, port 5000")
        app.debug = True
        app.run(use_reloader=False)

    def is_valid_login(username, password):
        if username in Server.loginTable: 
            return Server.loginTable[username] == password
        else:
            return False
    
    def log_the_user_in(name):
        return render_template('successful_login.html', name=name)
    
    def dont_log_the_user_in(name):
        return render_template('unsuccessful_login.html', name=name)
    
    
    @app.route('/')
    def try_to_login(name=None):
        return render_template('try_to_login.html', name=name)
    
    @app.route('/login', methods=['POST', 'GET'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
        if request.method == 'GET':
            username = request.args.get('username', None)
            password = request.args.get('password', None)
        if not username:
            return Server.try_to_login()
        elif Server.is_valid_login(username, password):
            return Server.log_the_user_in(username)
        else:
            return Server.dont_log_the_user_in(username)


def client():
    wait.untilServerRunning("127.0.0.1", 5000)
    print("client up and running")
    browser = webbrowser.get('firefox')
    urls = ['http://localhost:5000/login?username=tom&password=mot',
            'http://localhost:5000/login?username=sue&password=incorrect',
            'http://localhost:5000/login?username=jim&password=mij',
            'http://localhost:5000/']
    for url in urls:
        time.sleep(5)
        webbrowser.open(url)

Thread(target=client).start()

if __name__ == "__main__":
    Server.start(app)
