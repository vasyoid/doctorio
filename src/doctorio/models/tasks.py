from . import db


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    hospital = db.Column(db.Unicode(), default="Clinic")
    address = db.Column(db.Unicode(), default="Undefined")
    name = db.Column(db.Unicode(), default="Ivanov")
    surname = db.Column(db.Unicode(), default="Ivan")


class DoneTask(db.Model):
    __tablename__ = "done_tasks"

    id = db.Column(db.Integer, db.ForeignKey('tasks.id'), primary_key=True)
    customer = db.Column(db.Integer, db.ForeignKey('customers.id'), primary_key=True)
    verdict = db.Column(db.Boolean, default=False)
