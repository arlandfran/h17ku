import json
from flask import Blueprint, request, Response
from werkzeug.security import generate_password_hash
from app import mongo

auth_bp = Blueprint("auth_bp", __name__, url_prefix="/auth")


@auth_bp.post("/register")
def register():
    """Handle user registration"""
    if request.method == "POST":
        data = request.get_json()
        # check if email or user already exists
        existing_email = mongo.db.users.find_one({"email": data["email"]})
        existing_user = mongo.db.users.find_one({"username": data["username"].lower()})
        if existing_email:
            return Response(
                json.dumps({"error": "email already exists", "type": "email"}),
                status=409,
                mimetype="application/json",
            )
        if existing_user:
            return Response(
                json.dumps({"error": "username already exists", "type": "username"}),
                status=409,
                mimetype="application/json",
            )
        new_user = {
            "email": data["email"],
            "username": data["username"],
            "password": generate_password_hash(data["password"]),
        }
        mongo.db.users.insert_one(new_user)
        return Response(
            json.dumps({"message": "new user created"}),
            status=201,
            mimetype="application/json",
        )
