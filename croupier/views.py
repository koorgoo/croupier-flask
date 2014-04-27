from flask import render_template
from flask.ext.restful import (Resource, fields,
    marshal_with, reqparse)

from .server import app, db, api
from .models import Card


@app.route('/')
def index():
    return 'It works!'


@app.route('/app/')
@app.route('/app')
def lets_rock():
    return render_template('app.html')


@app.route('/test/')
@app.route('/test')
def test_js():
    return render_template('test.html')


# API

card_fields = {
    'id':    fields.Integer,
    'front': fields.String,
    'back':  fields.String
}

card_parser = reqparse.RequestParser()
card_parser.add_argument('id', type=int)
card_parser.add_argument('front', type=str)
card_parser.add_argument('back', type=str)


class Cards(Resource):
    @marshal_with(card_fields)
    def get(self):
        return Card.query.all()

    @marshal_with(card_fields)
    def post(self):
        args = card_parser.parse_args()
        args.pop('id')  # new card
        card = Card(**args)
        db.session.add(card)
        db.session.commit()
        return card, 201

api.add_resource(Cards, '/api/cards')
