from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from config import config

mongo = PyMongo()
login_manager = LoginManager()
login_manager.session_protection = "strong"


def create_app(config_name="dev"):
    """Create Flask app with specified config."""
    app = Flask(
        __name__,
        template_folder="../dist",
        static_folder="../dist/assets",
    )
    app.config.from_object(config.get(config_name))

    from api import api_bp

    app.register_blueprint(api_bp)

    mongo.init_app(app)
    login_manager.init_app(app)
    csrf = CSRFProtect(app)

    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def catch_all(path):
        """Catch all routes and serve index.html from /dist"""
        return render_template("index.html")

    return app