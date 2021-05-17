from flask import Flask
from flask import render_template
from flask import jsonify
from random import randrange
from flask import json
from flask import request


app = Flask(__name__)

def gen():
    while True:
        n = randrange(2, 11)
        if n !=5 and n !=10: yield n


@app.route('/answer', methods=["GET"])
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
        message = "---"
        
    n1 = next(g)
    n2 = next(g)
    data = {'n1':n1, 'n2':n2, 'message':message}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/tables')
def tables():
    data = request.args.get('result')
    print(data)
    n1 = next(g)
    n2 = next(g)
    return render_template('question.html', n1=n1, n2=n2, message="xxx")

@app.route('/question')
def question():
    n1 = next(g)
    n2 = next(g)
    data = {'n1':n1, 'n2':n2, 'message':''}
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    print("serving on localhost, port 5000")
    g = gen()
    app.run()
    app.run(debug=True, use_reloader=False)

