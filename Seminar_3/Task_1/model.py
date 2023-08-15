from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Boolean, nullable=False)
    group = db.Column(db.String(30), nullable=False)
    faculty_id = db.Column(db.ForeignKey('faculty.id'), nullable=False)

    def __repr__(self):
        return f'User({self.name}, {self.surmane})'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    # ссылка на студента
    student = db.relationship('Student', backref='faculty', lazy=True)

    def __repr__(self):
        return f'Faculty({self.name})'








