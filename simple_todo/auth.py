from flask_login.login_manager import LoginManager
from flask_login import login_user, logout_user, login_required, current_user
from flask.blueprints import Blueprint
from flask import request, render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .db import User, engine
from .form import LoginForm, SignUpForm, ChangePasswordForm

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

bp = Blueprint("auth", __name__, url_prefix="/auth")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@bp.route("/login", methods=("GET", "POST"))
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        email = request.form.get("email")
        password = request.form.get("password")
        remember_me = True if request.form.get("remember_me") else False

        user = User.query.filter_by(email=email).first()
        if not user:
            flash("bad login")
            return render_template("auth/login.html", form=login_form)
        
        if not check_password_hash(user.password, password):
            flash("bad login")
            return render_template("auth/login.html", form=login_form)
        
        login_user(user, remember=remember_me)
        next = request.args.get("next", None)
        return redirect(next or url_for("todo.index"))
    return render_template("auth/login.html", form=login_form)


@bp.route("/signup", methods=("GET", "POST"))
def signup():
    signup_form = SignUpForm()
    if signup_form.validate_on_submit():
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        password_retype = request.form.get("password_retype")

        user = User.query.filter_by(username=username, email=email).first()
        if user:
            flash("user already exists.")
            return render_template("auth/signup.html", form=signup_form)
        
        new_user = User(username=username, email=email, password=generate_password_hash(password))
        engine.session.add(new_user)
        engine.session.commit()
        flash("signup successful.")
        return redirect(url_for("auth.login"))
        
    return render_template("auth/signup.html", form=signup_form)


@bp.route("/changepassword", methods=["GET", "POST"])
def changepassword():
    change_password_form = ChangePasswordForm()
    if change_password_form.validate_on_submit():
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")

        user = User.query.get(int(current_user.id))
        if not user:
            abort(400)

        if not check_password_hash(user.password, old_password):
            flash("old password incorrect.")
            return render_template("auth/changepassword.html", form=change_password_form)
        
        user.password = generate_password_hash(new_password)
        engine.session.commit()
        flash("password updated.")
        return redirect(url_for("auth.logout"))
    return render_template("auth/changepassword.html", form=change_password_form)


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("logged out.")
    return redirect(url_for('auth.login'))