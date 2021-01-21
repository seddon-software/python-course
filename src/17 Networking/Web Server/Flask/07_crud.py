# pip install flask-sqlalchemy

# Building a CRUD application with Flask and SQLAlchemy
# Gareth Dwyer

from threading import Thread
from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import webbrowser
import wait


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(app)

class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)


class Server:    
    def __init__(self, app):
        print("serving on localhost, port 5000")
        app.debug = True
        app.run(use_reloader=False)
        Server.app = app
        
    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.form:
            book = Book(title=request.form.get("title"))
            db.session.add(book)
            db.session.commit()
        books = Book.query.all()
        return render_template("home.html", books=books)
    
    @app.route("/update", methods=["POST"])
    def update():
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()
        return redirect("/")
    @app.route("/delete", methods=["POST"])
    def delete():
        title = request.form.get("title")
        book = Book.query.filter_by(title=title).first()
        db.session.delete(book)
        db.session.commit()
        return redirect("/")

def client():
    wait.untilServerRunning("127.0.0.1", 5000)
    print("client up and running")
    browser = webbrowser.get('firefox')
    browser.open(f'http://localhost:5000/')


Thread(target=client).start()
db.create_all()


if __name__ == "__main__":
    Server(app)

