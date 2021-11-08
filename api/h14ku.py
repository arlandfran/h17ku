import os
import json
import pymongo
from bson import json_util
from dotenv import load_dotenv
from flask import Flask, request, Response
from werkzeug.security import generate_password_hash

load_dotenv()

app = Flask(__name__, static_folder="../dist", static_url_path="/")
client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
db = client.h14ku


def parse_json(data):
    """Parse data input into JSON"""
    return json.loads(json_util.dumps(data))


@app.route("/", defaults={"path": ""})
@app.route("/<string:path>")
def catch_all(path):
    """
    Catch all routes manually and serve index.html from dist.
    """
    return app.send_static_file("index.html")


@app.post("/api/auth/register")
def register():
    """
    Handle user registration
    """
    if request.method == "POST":
        data = request.get_json()

        # check if email or user already exists
        existing_email = db.users.find_one({"email": data["email"]})
        existing_user = db.users.find_one({"username": data["username"].lower()})

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

        db.users.insert_one(new_user)

        return Response(
            json.dumps({"message": "new user created"}),
            status=201,
            mimetype="application/json",
        )
