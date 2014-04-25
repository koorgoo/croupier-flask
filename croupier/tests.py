import os
os.environ['FLASK_ENV'] = 'test'

import json
import unittest

from croupier.server import app, db
from croupier.models import Card


class TestCase(unittest.TestCase):
  def setUp(self):
    db.create_all()
    db.session.add(Card('1 + 2 = ?', '3'))
    db.session.commit()
    self.app = app.test_client()

  def tearDown(self):
    db.drop_all()


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


if __name__ == '__main__':
  unittest.main()
