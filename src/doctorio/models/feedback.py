from . import db


class Feedback(db.Model):
    __tablename__ = "feedback"

    doctor = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    rating = db.Column(db.Integer, default=5)
    comment = db.Column(db.Unicode, default="")
