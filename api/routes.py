import json

from app import mongo
from app.helpers import parse_json
from api import api_bp


@api_bp.get("/posts")
def get_posts():
    posts = mongo.db.posts.find({})
    data = parse_json(posts)
    return {"data": data}, 200
