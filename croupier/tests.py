import os
os.environ['FLASK_ENV'] = 'test'

import json
import unittest

from flask.ext.login import current_user

from croupier.server import app, db
from croupier.models import Card, User


class TestCase(unittest.TestCase):
    def setUp(self):
        db.create_all()

        self.card = Card('1 + 2 = ?', '3')
        self.user = User('user', 'pass', 'user@test.com')

        db.session.add(self.card)
        db.session.add(self.user)
        db.session.commit()

        self.app = app.test_client()

    def tearDown(self):
        db.drop_all()

    def login(self):
        data = { 'username': 'user', 'password': 'pass' }
        self.app.post('/api/login', data=data)


class FooTest(TestCase):
    def test_env(self):
        assert os.environ['FLASK_ENV'] == 'test'

    def test_cards(self):
        assert Card.query.count() == 1


def json_loads(b):
    return json.loads(b.decode('utf8'))


class CardApiTest(TestCase):
    def test_retrieve_all(self):
        resp = self.app.get('/api/cards')
        data = json_loads(resp.data)
        assert resp.status_code == 200
        assert len(data) == 1

    def test_login_required_to_create_card(self):
        data = { 'front': '2 * 3 = ?', 'back': '6' }
        resp = self.app.post('/api/cards', data=data)
        assert resp.status_code == 401

    def test_create_card(self):
        self.login()
        data = { 'front': '2 * 3 = ?', 'back': '6' }
        resp = self.app.post('/api/cards', data=data)
        data = json_loads(resp.data)
        assert resp.status_code == 201
        assert data['back'] == '6'
        assert data['id'] is not None


class LoginApiTest(TestCase):
    def test_login(self):
        data = { 'username': self.user.username, 'password': self.user.password }
        resp = self.app.post('/api/login', data=data)
        assert resp.status_code == 200

    def test_bad_request(self):
        resp = self.app.post('/api/login', data={})
        assert resp.status_code == 400

    def test_unauthorized(self):
        data = { 'username': 'none', 'password': 'none' }
        resp = self.app.post('/api/login', data=data)
        assert resp.status_code == 401


if __name__ == '__main__':
  unittest.main(failfast=True)
