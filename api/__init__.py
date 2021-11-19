from flask import Blueprint
from flask_wtf.csrf import CSRFError

from api.auth import auth_bp

api_bp = Blueprint("api_bp", __name__, url_prefix="/api")
api_bp.register_blueprint(auth_bp)


@api_bp.errorhandler(CSRFError)
def handle_csrf_error(error):
    return {"msg": error.description}, 400


from api import routes
