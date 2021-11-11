from flask import Blueprint, request
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from app import mongo
from app.models import User


auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")


@auth_bp.post("/register")
def register():
    """Handle user registration"""
    data = request.get_json()
    # check if email or user already exists
    email_exists = mongo.db.users.find_one({"email": data["email"]})
    user_exists = mongo.db.users.find_one({"username": data["username"].lower()})
    if email_exists:
        return {"error": "email already exists", "type": "email"}, 409
    if user_exists:
        return {"error": "username already exists", "type": "username"}, 409
    new_user = {
        "email": data["email"],
        "username": data["username"].lower(),
        "pwd_hash": generate_password_hash(data["password"]),
    }
    mongo.db.users.insert_one(new_user)
    return {"message": "new user created"}, 201


@auth_bp.post("/login")
def login():
    """Handle user login"""
    data = request.get_json()
    email_exists = mongo.db.users.find_one({"email": data["email"]})
    if email_exists:
        if check_password_hash(email_exists["pwd_hash"], data["password"]):
            user_obj = User(
                email=data["email"],
                username=email_exists["username"],
                pwd_hash=email_exists["pwd_hash"],
            )
            login_user(user_obj)
            return {"login": True}, 200
        else:
            return {"login": False, "error": "incorrect password"}, 401
    else:
        return {"login": False, "error": "email not found"}, 404


@auth_bp.get("/session")
def check_session():
    """Check if user is logged in"""
    if current_user.is_authenticated:
        return {"login": True, "id": current_user.get_id()}, 200
    return {"login": False}


@auth_bp.get("/logout")
@login_required
def logout():
    """Handle user logout"""
    logout_user()
    return {"logout": True}, 200
