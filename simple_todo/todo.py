from flask.blueprints import Blueprint
from flask import render_template, request, abort, redirect, url_for
from .db import engine, TodoItem

bp = Blueprint("todo", __name__, url_prefix="/todo")


@bp.route("/")
def index():
    fresh_todos = TodoItem.query.filter(TodoItem.is_finished==False).all()
    return render_template("todo/index.html", todos=fresh_todos)


@bp.route("/history")
def history():
    page = request.args.get("page", 1)
    return render_template("todo/history.html")



@bp.route("/create", methods=["POST", ])
def create_todo():
    new_todo_text = request.form.get("new-todo", None)
    if new_todo_text is None or new_todo_text.strip() == "":
        abort(400)
    
    new_todo = TodoItem(text=new_todo_text)

    try:
        engine.session.add(new_todo)
        engine.session.commit()
        return redirect(url_for("todo.index"))
    except:
        abort(400)



@bp.route("/finish", methods=["POST", ])
def finish_todo():
    """
    docstring
    """
    pass