from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from flask_login import LoginManager, current_user
from flask_wtf.csrf import CSRFProtect

mongo = PyMongo()
login_manager = LoginManager()
login_manager.session_protection = "strong"


def create_app(config="config.DevConfig"):
    """Create Flask app with specified config."""
    app = Flask(
        __name__,
        template_folder="../dist",
        static_folder="../dist/assets",
    )
    app.config.from_object(config)

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

    @app.route("/login")
    def redirect_login():
        if current_user.is_authenticated:
            return redirect("/")
        else:
            return render_template("index.html")

    @app.route("/register")
    def redirect_register():
        if current_user.is_authenticated:
            return redirect("/")
        else:
            return render_template("index.html")

    return app
