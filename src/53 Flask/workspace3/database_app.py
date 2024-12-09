import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =        'sqlite:///' + os.path.join(basedir, 'database.db')
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    homeTeam = db.Column(db.String(100), nullable=False)
    homeScore = db.Column(db.Integer)
    awayTeam = db.Column(db.String(100), nullable=False)
    awayScore = db.Column(db.Integer)

    def play(self, home, score1, away, score2):
        self.homeTeam = home
        self.homeScore = score1
        self.awayTeam = away
        self.awayScore = score2
        
    def __str__(self):
        return f"{self.homeTeam} {self.homeScore}-{self.awayScore} {self.awayTeam}"

@app.route('/')
def index():
    matches = Match.query.all()
    return render_template('index.html', matches=matches)

@app.route('/<int:match_id>/')
def singleMatch(match_id):
    match = Match.query.get_or_404(match_id)
    return render_template('singleMatch.html', match=match, id=match_id)

@app.route('/create/', methods=('GET', 'POST'))
@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        homeTeam = request.form['homeTeam']
        awayTeam = request.form['awayTeam']
        homeScore = request.form['homeScore']
        awayScore = request.form['awayScore']

        match = Match()
        match.play(homeTeam, homeScore, awayTeam, awayScore)
        db.session.add(match)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create.html')
