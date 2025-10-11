from flask import Flask
from threading import Thread, Timer
import logging
import time
import numpy as np

SLEEP = 1
logging.getLogger('werkzeug').setLevel(logging.ERROR)
temperatures = list(np.arange(18.0, 25.0, 0.1))

app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=False)


def myfunc():
    while len(temperatures) > 0:
        t = Timer(SLEEP, temperatures.pop(0))
        time.sleep(SLEEP)

@app.route('/start')
def index():
    worker = Thread(target=myfunc)
    worker.start()
    return 'This is the FLASK app index page'


@app.route('/getTemperature')
def getTemperature():
    time.sleep(SLEEP)
    try:
        temperature = temperatures[0]
    except:
        temperature = None
    return str(temperature)

