from datetime import datetime
from bson import ObjectId
from flask import request
from flask_login import login_required

from app import mongo
from app.helpers import parse_json
from api import api_bp


@api_bp.get("/comments")
def get_comments():
    _id = request.args.get("id")
    data = mongo.db.comments.find({"post": ObjectId(_id)})
    return {"data": parse_json(data)}, 200


@api_bp.post("/comment")
def post_comment():
    p_id = request.args.get("id")
    data = request.json
    time = datetime.now()
    comment = {
        "post": ObjectId(p_id),
        "username": data["username"],
        "comment": data["comment"],
        "posted_at": time,
        "likes": [],
        "edited": False,
    }
    mongo.db.comments.insert_one(comment)
    document = mongo.db.comments.find_one({"posted_at": time})
    mongo.db.posts.update_one(
        {"_id": ObjectId(p_id)}, {"$push": {"comments": document["_id"]}}
    )
    return {"posted": parse_json(comment)}, 200


@api_bp.put("/comment")
@login_required
def update_comment():
    _id = request.args.get("id")
    data = request.json
    mongo.db.comments.update_one(
        {"_id": ObjectId(_id)},
        {"$set": {"comment": data["comment"], "edited": True}},
    )
    return {}, 204


@api_bp.delete("/comment")
@login_required
def delete_comment():
    p_id = request.args.get("pid")
    c_id = request.args.get("cid")
    mongo.db.posts.update_one(
        {"_id": ObjectId(p_id)}, {"$pull": {"comments": ObjectId(c_id)}}
    )
    mongo.db.comments.delete_one({"_id": ObjectId(c_id)})
    return {}, 204


@api_bp.patch("/comment")
@login_required
def like_comment():
    _id = request.args.get("id")
    like = request.args.get("like")
    username = request.json["username"]
    if like == "true":
        mongo.db.comments.update_one(
            {"_id": ObjectId(_id)},
            {"$push": {"likes": username}},
        )
        return {"liked": True}, 200
    if like == "false":
        mongo.db.comments.update_one(
            {"_id": ObjectId(_id)},
            {"$pull": {"likes": username}},
        )
        return {"liked": False}, 200
    return {}, 400
