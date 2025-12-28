import os
os.chdir("..")
os.system("pwd")

from flask import Flask
from flask import render_template, url_for, send_from_directory

app = Flask(__name__, template_folder="/templates")


@app.route("/memory6")
def hello():
#    url_for('static', filename='/clock.js')
    return render_template('memory6.html')
'''
@app.route('/css/<path:filename>')
def base_static(filename):
    return send_from_directory(app.root_path + '/images/cards/', filename)

@app.route('/jq/<path:filename>')
def base_static2(filename):
    return send_from_directory(app.root_path + '/jq/', filename)
'''

'''
@app.route('/images/<path:filename>')
def base_static(filename):
    return send_from_directory(app.root_path + '/images/', filename)
'''

# run the application
if __name__ == "__main__":
    app.run(debug=True)
