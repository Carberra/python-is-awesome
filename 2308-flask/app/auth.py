from functools import wraps

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.security import check_password_hash, generate_password_hash

from app.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        db = get_db()

        username = request.form["username"]
        password = request.form["password"]
        error = None

        if not username:
            error = "Username is required."
        elif not password:
            error = "Password is required."

        if not error:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
                return redirect(url_for("auth.login"))
            except db.IntegrityError:
                error = f"User {username!r} is already taken. Please try another."

        flash(error, category="error")

    return render_template("auth/register.html")


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        db = get_db()

        username = request.form["username"]
        password = request.form["password"]
        error = None

        user = db.execute(
            "SELECT * FROM user WHERE username = ?", (username,)
        ).fetchone()

        if not user:
            error = "Incorrect username."
        elif not check_password_hash(user["password"], password):
            error = "Incorrect password."

        if not error:
            session.clear()
            session["user_id"] = user["id"]
            return redirect("/")

        flash(error, category="error")

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))


@bp.before_app_request
def get_logged_in_user():
    g.user = (
        get_db().execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        if (user_id := session.get("user_id"))
        else None
    )


def login_required(view):
    @wraps(view)
    def wrapper(**kwargs):
        return view(**kwargs) if g.user else redirect(url_for("auth.login"))

    return wrapper
