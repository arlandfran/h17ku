import random
from flask import request

from app import mongo
from app.helpers import parse_json
from app.haikus import haikus
from api import api_bp


@api_bp.get("/user")
def get_user():
    username = request.args.get("username")
    if username:
        user = mongo.db.users.find_one({"username": username})
        if user:
            posts = (
                mongo.db.posts.find({"username": username})
                .sort("posted_at", -1)
                .limit(10)
            )
            if not posts:
                return {"data": []}, 200
            data = parse_json(posts)
            return {"data": data}, 200
        return {"msg": "username not found"}, 404
    return {}, 400


@api_bp.get("/haiku")
def get_error_haiku():
    haiku = random.choice(haikus)
    return {"data": haiku}, 200


from api import posts, comments
