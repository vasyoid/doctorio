from . import db


class Hospital(db.Model):
    __tablename__ = "hospitals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(), default="Clinic")
    address = db.Column(db.Unicode(), default="Undefined")


class Doctor(db.Model):
    __tablename__ = "doctors"

    id = db.Column(db.Integer, primary_key=True)
    hospital = db.Column(db.Integer, db.ForeignKey('hospitals.id'))
    name = db.Column(db.Unicode(), default="Ivanov")
    surname = db.Column(db.Unicode(), default="Ivan")
    cost = db.Column(db.Integer, default=0)


class Competence(db.Model):
    __tablename__ = "competences"

    doctor = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    title = db.Column(db.Unicode(), default="physician")


class Slots(db.Model):
    __tablename__ = "slots"

    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))
    timestemp = db.Column(db.Integer, default=0)
