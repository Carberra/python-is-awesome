from flask import Blueprint, render_template, send_file

bp = Blueprint("data", __name__, url_prefix="/data")


@bp.route("/view", methods=("GET",))
def view():
    return render_template("data/view.html")


@bp.route("/<string:filename>", methods=("GET",))
def file(filename):
    return send_file(f"static/data/{filename}")
