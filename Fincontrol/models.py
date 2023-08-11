from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Reestr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer, nullable=False)
    process_id = db.Column(db.Integer, db.ForeignKey('process.id'), nullable=False)


    # first_name = db.Column(db.String(80), nullable=False)
    # last_name = db.Column(db.String(80), nullable=False)
    # age = db.Column(db.Integer)
    # group = db.Column(db.Integer)
    # gender = db.Column(db.String(20), nullable=False)
    # faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'), nullable=False)


    def __repr__(self):
        return f'{self.id} {self.code}'



# class Faculty(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     students = db.relationship('Student', backref='faculty', lazy=True)


class Process (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, nullable=False)
    reestr = db.relationship('Reestr', backref='process', lazy=True)

    def __repr__(self):
        return f'{self.name}'


# class Operation (db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), unique=True, nullable=False)
#
#
# class Dolj (db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), unique=True, nullable=False)
#
#
# class Kontrdet (db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), unique=True, nullable=False)
#
#
# class Method (db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128), unique=True, nullable=False)
#
#
