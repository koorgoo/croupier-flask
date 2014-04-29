from flask import request, render_template
from flask.ext.login import (login_user, login_required,
    current_user)
from flask.ext.restful import (Resource, fields,
    marshal_with, reqparse, abort)

from .server import app, db, api, login_manager
from .models import Card, User


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

    @login_required
    @marshal_with(card_fields)
    def post(self):
        args = card_parser.parse_args()
        args.pop('id')  # new card
        card = Card(**args)
        db.session.add(card)
        db.session.commit()
        return card, 201

api.add_resource(Cards, '/api/cards')


user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
}


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class Login(Resource):
    @marshal_with(user_fields)
    def post(self):
        u = request.form.get('username')
        p = request.form.get('password')
        if not u or not p:
            return abort(400)

        user = User.query.filter_by(username=u, password=p).first()
        if user is not None:
            login_user(user)
            return user
        return abort(401)

api.add_resource(Login, '/api/login')


class Me(Resource):
    @login_required
    @marshal_with(user_fields)
    def get(self):
        return current_user

api.add_resource(Me, '/api/me')
