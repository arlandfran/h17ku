from datetime import datetime
from bson import ObjectId
from flask import request
from flask_login import login_required

from app import mongo
from app.helpers import parse_json
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
                mongo.db.posts.find({"username": username})
                .sort("posted_at", -1)
                .limit(10)
            )
            data = parse_json(posts)
            return {"data": data}, 200
    return {"msg": "filter argument missing"}, 400


@api_bp.get("/post")
def get_post():
    _id = request.args.get("id")
    document = mongo.db.posts.find_one({"_id": ObjectId(_id)})
    data = parse_json(document)
    return {"data": data}, 200


@api_bp.post("/post")
@login_required
def post():
    data = request.json
    document = {
        "username": data["username"],
        "haiku": data["haiku"],
        "posted_at": datetime.now(),
        "likes": [],
        "comments": [],
        "edited": False,
    }
    mongo.db.posts.insert_one(document)
    return {"posted": document}, 200


@api_bp.put("/post")
@login_required
def update_post():
    _id = request.args.get("id")
    data = request.json
    mongo.db.posts.update_one(
        {"_id": ObjectId(_id)},
        {"$set": {"haiku": data["haiku"], "edited": True}},
    )
    return {}, 204


@api_bp.delete("/post")
@login_required
def delete_post():
    _id = request.args.get("id")
    mongo.db.posts.delete_one({"_id": ObjectId(_id)})
    return {}, 204


@api_bp.patch("/post")
@login_required
def like_post():
    _id = request.args.get("id")
    like = request.args.get("like")
    username = request.json["username"]
    if like == "true":
        mongo.db.posts.update_one(
            {"_id": ObjectId(_id)},
            {"$push": {"likes": username}},
        )
        return {"liked": True}, 200
    if like == "false":
        mongo.db.posts.update_one(
            {"_id": ObjectId(_id)},
            {"$pull": {"likes": username}},
        )
        return {"liked": False}, 200
    return {}, 400
