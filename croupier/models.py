from .server import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.Text)
    back = db.Column(db.Text)

    def __init__(self, front, back):
        self.front = front
        self.back = back

    def __repr__(self):
        return '<Card %r>' % self.id
