from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime

engine = SQLAlchemy()


class TodoItem(engine.Model):
    id = engine.Column(engine.Integer, primary_key=True)
    text = engine.Column(engine.String(200), nullable=False)
    is_finished = engine.Column(engine.Boolean, nullable=False, default=False)
    created_at = engine.Column(engine.DateTime, default=datetime.datetime.now)
    finished_at = engine.Column(engine.DateTime, nullable=True)
    
    user_id = engine.Column(engine.Integer, engine.ForeignKey('user.id'), nullable=False)
    user = engine.relationship('User', backref=engine.backref('todos', lazy=True))

    def __repr__(self):
        return f"<todo item id: {self.id} text: {self.text}>"


class User(UserMixin, engine.Model):
    id = engine.Column(engine.Integer, primary_key=True)
    username = engine.Column(engine.String(200), nullable=False, unique=True)
    email = engine.Column(engine.String(200), nullable=False, unique=True)
    password = engine.Column(engine.String(200), nullable=False)
    created_at = engine.Column(engine.DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f"<user id: {self.id} username: {self.username}>"