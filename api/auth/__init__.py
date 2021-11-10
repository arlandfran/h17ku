from flask import Blueprint, request
from werkzeug.security import check_password_hash, generate_password_hash
from app import mongo

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")


@auth_bp.post("/register")
def register():
    """Handle user registration"""
    if request.method == "POST":
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
            "username": data["username"],
            "password": generate_password_hash(data["password"]),
        }
        mongo.db.users.insert_one(new_user)
        return {"message": "new user created"}, 201


@auth_bp.post("/login")
def login():
    """Handle user login"""
    if request.method == "POST":
        data = request.get_json()
        email = mongo.db.users.find_one({"email": data["email"]})
        if email:
            if check_password_hash(email["password"], data["password"]):
                return {"message": "login successful"}, 200
            else:
                return {"error": "incorrect password"}, 401
        else:
            return {"error": "email not found"}, 404
