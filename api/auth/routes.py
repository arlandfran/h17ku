from flask import request
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash

from app import mongo
from app.models import User, NewUserSchema, UserSchema
from app.helpers import find_whitespace
from api.auth import auth_bp


@auth_bp.post("/register")
def register():
    """Handle user registration"""
    data = request.get_json()
    # validate json data
    if find_whitespace(data):
        return {"msg": "no spaces allowed"}, 400
    invalid = NewUserSchema().validate(data)
    if invalid:
        return {"msg": invalid}, 400
    if data["password"] != data["password2"]:
        return {"msg": "passwords do not match"}, 400
    # check if email or user already exists
    email_exists = mongo.db.users.find_one({"email": data["email"]})
    user_exists = mongo.db.users.find_one({"username": data["username"].lower()})
    if email_exists:
        return {"msg": "email already exists", "errorField": "email"}, 409
    if user_exists:
        return {"msg": "username already exists", "errorField": "username"}, 409
    new_user = {
        "email": data["email"],
        "username": data["username"].lower(),
        "pwd_hash": generate_password_hash(data["password"]),
    }
    mongo.db.users.insert_one(new_user)
    return {"msg": "new user created"}, 201


@auth_bp.post("/login")
def login():
    """Handle user login"""
    data = request.get_json()
    if find_whitespace(data):
        return {"msg": "no spaces allowed"}, 400
    invalid = UserSchema().validate(data)
    if invalid:
        return {"msg": invalid}, 400
    email_exists = mongo.db.users.find_one({"email": data["email"]})
    if email_exists:
        if check_password_hash(email_exists["pwd_hash"], data["password"]):
            user_obj = User(
                email=data["email"],
                username=email_exists["username"],
            )
            login_user(user_obj)
            return {"login": True}, 200
        else:
            return {"login": False, "msg": "incorrect password"}, 401
    else:
        return {"login": False, "msg": "email not found"}, 404


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
