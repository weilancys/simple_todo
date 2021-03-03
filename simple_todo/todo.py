from flask.blueprints import Blueprint
from flask import render_template, request, abort, redirect, url_for, current_app
from flask_login import login_required
from .db import engine, TodoItem
import datetime
import math

bp = Blueprint("todo", __name__, url_prefix="/todo")


@bp.route("/")
def index():
    fresh_todos = TodoItem.query.filter(TodoItem.is_finished==False).all()
    return render_template("todo/index.html", todos=fresh_todos)


@bp.route("/history")
def history():
    try:
        page = int(request.args.get("page", 1))
    except:
        abort(400)

    finished_todos_count = TodoItem.query.filter_by(is_finished=True).count()
    page_count = math.ceil(finished_todos_count / current_app.config["TODO_ITEMS_MAX_PER_PAGE"])
    start_id = (page - 1) * current_app.config["TODO_ITEMS_MAX_PER_PAGE"] + 1
    end_id = start_id + current_app.config["TODO_ITEMS_MAX_PER_PAGE"]
    finished_todos = TodoItem.query.filter_by(is_finished=True).order_by(TodoItem.finished_at.desc()).slice(start_id - 1, end_id - 1).all()

    ctx = {
        "todos": finished_todos,
        "pagination": {
            "page": page,
            "prev": "#" if page <= 1 else url_for("todo.history", page=page-1),
            "next": "#" if page >= page_count else url_for("todo.history", page=page+1),
            "page_count": page_count,
        }
    }
    return render_template("todo/history.html", ctx=ctx)



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
    ids = request.form.getlist("todo-item")
    try:
        for _id in ids:
            todo_item = TodoItem.query.get(int(_id))
            todo_item.is_finished = True
            todo_item.finished_at = datetime.datetime.now()
        engine.session.commit()
        return redirect(url_for("todo.index"))
    except:
        engine.session.rollback()
        abort(400)

