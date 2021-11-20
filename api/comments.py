from bson import ObjectId
from datetime import datetime
from flask import request
from flask_login import login_required

from app import mongo
from app.helpers import parse_json
from api import api_bp


@api_bp.get("/comments")
def get_comments():
    _id = request.args.get("id")
    comments = mongo.db.posts.find_one(
        {"_id": ObjectId(_id)}, {"comments": 1, "_id": 0}
    )
    json = parse_json(comments)
    oids = []
    for _id in json["comments"]:
        oids.append(ObjectId(_id["$oid"]))
    data = mongo.db.comments.find({"_id": {"$all": oids}})
    return {"data": parse_json(data)}, 200


@api_bp.post("/comment")
def post_comment():
    _id = request.args.get("id")
    data = request.json
    document = mongo.db.posts.find_one({"_id": ObjectId(_id)})
    if document:
        _id = ObjectId()
        new_comment = {
            "_id": _id,
            "username": data["username"],
            "comment": data["comment"],
            "posted_at": datetime.now(),
            "likes": [],
            "edited": False,
        }
        mongo.db.posts.update_one({"_id": ObjectId(_id)}, {"$push": {"comments": _id}})
        mongo.db.comments.insert_one(new_comment)
        return {"posted": new_comment}, 200
    return {}, 400


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
