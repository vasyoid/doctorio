from . import db


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(), default="Ivanov")
    surname = db.Column(db.Unicode(), default="Ivan")
    misses = db.Column(db.Integer, default=0)
    bonuses = db.Column(db.Integer, default=100)
