from flask import render_template

from .server import app
from .models import Card


@app.route('/')
def index():
    return 'It works!'


@app.route('/cards')
def cards():
    cards = Card.query.all()
    return render_template('cards.html', cards=cards)
