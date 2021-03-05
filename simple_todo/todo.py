from flask.blueprints import Blueprint
from flask import render_template, request, abort, redirect, url_for, current_app
from flask_login import login_required, current_user
from .db import engine, TodoItem
from .form import NewTodoForm, TodoListForm
import datetime
import math

bp = Blueprint("todo", __name__, url_prefix="/todo")


@bp.route("/")
@login_required
def index():
    fresh_todos = TodoItem.query.filter(TodoItem.is_finished==False, TodoItem.user_id==current_user.id).all()
    return render_template("todo/index.html", todos=fresh_todos, new_todo_form=NewTodoForm(), todo_list_form=TodoListForm())


@bp.route("/history")
@login_required
def history():
    try:
        page = int(request.args.get("page", 1))
    except:
        abort(400)

    finished_todos_count = TodoItem.query.filter_by(is_finished=True, user_id=current_user.id).count()
    page_count = math.ceil(finished_todos_count / current_app.config["TODO_ITEMS_MAX_PER_PAGE"])
    start_id = (page - 1) * current_app.config["TODO_ITEMS_MAX_PER_PAGE"] + 1
    end_id = start_id + current_app.config["TODO_ITEMS_MAX_PER_PAGE"]
    finished_todos = TodoItem.query.filter_by(is_finished=True, user_id=current_user.id).order_by(TodoItem.finished_at.desc()).slice(start_id - 1, end_id - 1).all()

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
@login_required
def create_todo():
    new_todo_form = NewTodoForm()
    if new_todo_form.validate_on_submit():
        new_todo_text = request.form.get("new_todo", None)
        new_todo = TodoItem(text=new_todo_text, user_id=current_user.id)
        try:
            engine.session.add(new_todo)
            engine.session.commit()
            return redirect(url_for("todo.index"))
        except Exception as e:
            print(str(e))
            abort(400)
    fresh_todos = TodoItem.query.filter(TodoItem.is_finished==False, TodoItem.user_id==current_user.id).all()
    return render_template("todo/index.html", todos=fresh_todos, new_todo_form=new_todo_form, todo_list_form=TodoListForm())



@bp.route("/finish", methods=["POST", ])
@login_required
def finish_todo():
    todo_list_form = TodoListForm()
    if todo_list_form.validate_on_submit():
        ids = request.form.getlist("todo-item")
        try:
            for _id in ids:
                todo_item = TodoItem.query.get(int(_id))
                if todo_item.user_id != current_user.id:
                    raise ValueError("error finishing todos that don't belong to current user.")
                todo_item.is_finished = True
                todo_item.finished_at = datetime.datetime.now()
            engine.session.commit()
            return redirect(url_for("todo.index"))
        except:
            abort(400)
    fresh_todos = TodoItem.query.filter(TodoItem.is_finished==False, TodoItem.user_id==current_user.id).all()
    return render_template("todo/index.html", todos=fresh_todos, new_todo_form=NewTodoForm(), todo_list_form=todo_list_form)

