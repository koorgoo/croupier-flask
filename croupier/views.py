from flask import render_template

from .server import app
from .models import Card


@app.route('/')
def index():
    return 'It works!'


@app.route('/app/')
@app.route('/app')
def lets_rock():
    return render_template('app.html')
