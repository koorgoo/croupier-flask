from flask import render_template
from flask.ext.restful import Resource, fields, marshal_with

from .server import app, api
from .models import Card


@app.route('/')
def index():
    return 'It works!'


@app.route('/app/')
@app.route('/app')
def lets_rock():
    return render_template('app.html')


# API

card_fields = {
    'id':    fields.Integer,
    'front': fields.String,
    'back':  fields.String
}

class Cards(Resource):
    @marshal_with(card_fields)
    def get(self):
        return Card.query.all()

api.add_resource(Cards, '/api/cards')
