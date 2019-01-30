from datetime import datetime
from app import login
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin




class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    logs = db.relationship('Log', backref='owner', lazy='dynamic')

    def __repr__(self):
        return 'User {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)




class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    log_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sessions = db.relationship('Session', backref='logname', lazy='dynamic')

    def __repr__(self):
        return 'Log {}'.format(self.name)
    


class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.Integer, db.ForeignKey('log.id'))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    exercises = db.relationship('Exercise', backref='sessname', lazy='dynamic')

    def __repr__(self):
        return 'Session {}'.format(self.timestamp)


class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    exercise_id = db.Column(db.Integer, db.ForeignKey('session.id'))
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    time = db.Column(db.Integer)
    RPE = db.Column(db.Integer)

    def __repr__(self):
        return 'Exercise {}'.format(self.name)

    
