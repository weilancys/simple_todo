from flask.blueprints import Blueprint
from flask import render_template, request

bp = Blueprint("todo", __name__, url_prefix="/todo")


@bp.route("/")
def index():
    return render_template("todo/index.html")


@bp.route("/history")
def history():
    page = request.args.get("page", 1)
    return render_template("todo/history.html")



@bp.route("/create", methods=["POST", ])
def create_todo():
    """
    docstring
    """
    pass


@bp.route("/finish", methods=["POST", ])
def finish_todo():
    """
    docstring
    """
    pass