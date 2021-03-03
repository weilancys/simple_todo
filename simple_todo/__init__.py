from flask import Flask, redirect, url_for
from . import todo
from . import db
from .auth import login_manager
import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # instance path
    os.makedirs(app.instance_path, exist_ok=True)

    # config
    app.config['SECRET_KEY'] = "dev"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, "test.db") 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['TODO_ITEMS_MAX_PER_PAGE'] = 20

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    # blueprints
    app.register_blueprint(todo.bp)
    @app.route("/")
    def redirect_to_todo():
        return redirect(url_for("todo.index"))

    # database
    db.engine.init_app(app)

    # login
    login_manager.init_app(app)

    return app