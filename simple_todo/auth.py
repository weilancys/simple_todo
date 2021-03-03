from flask_login.login_manager import LoginManager
from flask.blueprints import Blueprint
from .db import User

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

bp = Blueprint("auth", __name__, url_prefix="/auth")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp.route("/login", methods=("GET", "POST"))
def login():
    pass


@bp.route("/signup", methods=("GET", "POST"))
def signup():
    pass


@bp.route("/logout")
def logout():
    pass