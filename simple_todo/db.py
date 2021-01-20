from flask_sqlalchemy import SQLAlchemy
import datetime

engine = SQLAlchemy()


class TodoItem(engine.Model):
    id = engine.Column(engine.Integer, primary_key=True)
    text = engine.Column(engine.String(200), nullable=False)
    is_finished = engine.Column(engine.Boolean, nullable=False, default=False)
    created_at = engine.Column(engine.DateTime, default=datetime.datetime.now)
    finished_at = engine.Column(engine.DateTime, nullable=True)

    def __repr__(self):
        return f"<todo item id: {self.id} text: {self.text}>"


class User(object):
    """
    docstring
    """
    pass