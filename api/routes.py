import random
from datetime import datetime
from bson import ObjectId
from flask import request
from flask_login import login_required

from app import mongo
from app.helpers import parse_json
from app.haikus import haikus
from api import api_bp


@api_bp.get("/posts")
def get_posts():
    post_filter = request.args.get("filter")
    if post_filter:
        if post_filter == "popular":
            posts = mongo.db.posts.find({}).sort("likes", -1).limit(10)
            data = parse_json(posts)
            return {"data": data}, 200
        if post_filter == "newest":
            posts = mongo.db.posts.find({}).sort("posted_at", -1).limit(10)
            data = parse_json(posts)
            return {"data": data}, 200
        if post_filter == "my-haikus":
            username = request.args.get("username")
            posts = (
                mongo.db.posts.find({"author": username})
                .sort("posted_at", -1)
                .limit(10)
            )
            data = parse_json(posts)
            return {"data": data}, 200
    return {"msg": "either no arguments given or the argument given is invalid"}, 400


@api_bp.get("/post")
def get_post():
    post_id = request.args.get("id")
    if post_id:
        document = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
        data = parse_json(document)
        return {"data": data}, 200
    return {"msg": "no id given"}, 400


@api_bp.post("/post")
@login_required
def post():
    if request.args.get("id"):
        post_id = request.args.get("id")
        data = request.json
        document = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
        if document:
            new_comment = {
                "username": data["username"],
                "comment": data["comment"],
                "posted_at": datetime.now(),
            }
            mongo.db.posts.update_one(
                {"_id": ObjectId(post_id)}, {"$push": {"comments": new_comment}}
            )
            return {"msg": "comment added"}, 200
        return {
            "msg": "either no arguments given or the argument given is invalid"
        }, 400
    data = request.json
    posted_at = datetime.now()
    document = {
        "author": data["author"],
        "haiku": data["haiku"],
        "posted_at": posted_at,
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
            posts = (
                mongo.db.posts.find({"author": username})
                .sort("posted_at", -1)
                .limit(10)
            )
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
