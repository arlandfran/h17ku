from flask import Flask
from flask_pymongo import PyMongo
from config import config


mongo = PyMongo()


def create_app(config_name="dev"):
    """Create Flask app with specified config."""
    app = Flask(__name__, static_folder="../dist", static_url_path="/")
    app.config.from_object(config.get(config_name))

    from api import api_bp

    app.register_blueprint(api_bp)

    mongo.init_app(app)

    @app.route("/", defaults={"path": ""})
    @app.route("/<string:path>")
    def catch_all(path):
        """Catch all routes manually and serve index.html from dist"""
        return app.send_static_file("index.html")

    return app
