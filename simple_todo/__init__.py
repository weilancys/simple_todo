from flask import Flask, redirect, url_for
from . import todo
from . import db
from .auth import login_manager


def create_app():
    app = Flask(__name__)

    # config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

    # blueprints
    app.register_blueprint(todo.bp)
    @app.route("/")
    def redirect_to_todo():
        return redirect(url_for("todo.index"))

    # database
    db.engine.init_app(app)

    # login
    # login_manager.init_app(app)

    return app