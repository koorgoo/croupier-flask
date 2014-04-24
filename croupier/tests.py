import os
os.environ['FLASK_ENV'] = 'test'

import unittest

from croupier.server import app, db
from croupier.models import Card


class TestCase(unittest.TestCase):
  def setUp(self):
    db.create_all()
    db.session.add(Card('1 + 2 = ?', '3'))
    db.session.commit()

  def tearDown(self):
    db.drop_all()


class FooTest(TestCase):
  def test_env(self):
    assert os.environ['FLASK_ENV'] == 'test'

  def test_cards(self):
    assert Card.query.count() == 1


if __name__ == '__main__':
  unittest.main()
