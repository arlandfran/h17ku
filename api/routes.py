from datetime import datetime
from flask import request
from flask_login import login_required

from app import mongo
from app.helpers import parse_json
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