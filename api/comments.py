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
    comments = mongo.db.posts.find_one(
        {"_id": ObjectId(_id)}, {"comments": 1, "_id": 0}
    )
    json = parse_json(comments)
    _ids = []
    for _id in json["comments"]:
        _ids.append(ObjectId(_id["$oid"]))
    data = mongo.db.comments.find({"_id": {"$all": _ids}})
    return {"data": parse_json(data)}, 200


@api_bp.post("/comment")
def post_comment():
    p_id = request.args.get("id")
    data = request.json
    _id = ObjectId()
    comment = {
        "_id": _id,
        "username": data["username"],
        "comment": data["comment"],
        "posted_at": datetime.now(),
        "likes": [],
        "edited": False,
    }
    mongo.db.posts.update_one({"_id": ObjectId(p_id)}, {"$push": {"comments": _id}})
    mongo.db.comments.insert_one(comment)
    return {"posted": comment}, 200


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
    mongo.db.posts.update_one({"_id": ObjectId(p_id)}, {"$pull": {"comments": c_id}})
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
