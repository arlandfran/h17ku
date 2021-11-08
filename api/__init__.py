from flask import Blueprint

from .auth import auth_bp

api_bp = Blueprint("api_bp", __name__, url_prefix="/api")
api_bp.register_blueprint(auth_bp)
