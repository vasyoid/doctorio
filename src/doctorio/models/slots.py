from . import db


class FreeSlot(db.Model):
    __tablename__ = "free_slots"

    doctor = db.Column(db.Integer, db.ForeignKey('doctors.id'), primary_key=True)
    timestamp = db.Column(db.Integer, default=5, primary_key=True)


class BusySlot(db.Model):
    __tablename__ = "busy_slots"

    doctor = db.Column(db.Integer, db.ForeignKey('doctors.id'), primary_key=True)
    timestamp = db.Column(db.Integer, default=5, primary_key=True)
    customer = db.Column(db.Integer, db.ForeignKey('customers.id'))
