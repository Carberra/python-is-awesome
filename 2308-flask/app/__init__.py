from pathlib import Path

from flask import Flask, render_template


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    instance_path = Path(app.instance_path)
    instance_path.mkdir(exist_ok=True)

    app.config.from_mapping(SECRET_KEY="dev", DB_PATH=instance_path / "app.sqlite")

    if test_config:
        app.config.from_mapping(test_config)
    else:
        app.config.from_pyfile("config.py", silent=True)

    @app.route("/")
    def _():
        return render_template("index.html")

    from . import auth, db

    db.init_app(app)
    app.register_blueprint(auth.bp)

    return app
