import random
from datetime import datetime
from flask import request
from flask_login import login_required

from app import mongo
from app.helpers import parse_json
from app.haikus import haikus
from api import api_bp


@api_bp.get("/posts")
def get_posts():
    posts = mongo.db.posts.find({}).sort("created_at", -1)
    data = parse_json(posts)
    return {"data": data}, 200


@api_bp.post("/post")
@login_required
def post():
    data = request.json
    created_at = datetime.now()
    document = {
        "author": data["author"],
        "haiku": data["haiku"],
        "created_at": created_at,
        "likes": 0,
    }
    mongo.db.posts.insert_one(document)
    return {"msg": "haiku posted successfully"}, 200


@api_bp.get("/user")
def get_user():
    username = request.args.get("username")
    if username:
        user = mongo.db.users.find_one({"username": username})
        if user:
            posts = mongo.db.posts.find({"author": username})
            if not posts:
                return {"data": []}, 200
            data = parse_json(posts)
            return {"data": data}, 200
        return {"msg": "username not found"}, 404
    return {"msg": "no username given"}, 400


@api_bp.get("/haiku")
def get_haiku():
    haiku = random.choice(haikus)
    return {"data": haiku}, 200
