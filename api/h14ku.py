import os
import time
import json
import pymongo
from bson import json_util
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__, static_folder="../dist", static_url_path="/")
client = pymongo.MongoClient(os.environ.get("MONGO_URI"))
db = client.h14ku


def parse_json(data):
    """Parse data input into JSON"""
    return json.loads(json_util.dumps(data))


@app.route("/")
def index():
    """Serve build bundle"""
    return app.send_static_file("index.html")


@app.route("/api/time")
def get_current_time():
    """Return current time in seconds"""
    return {"time": time.time()}


@app.route("/api/users")
def get_all_users():
    """Return all documents in users collection"""
    users = db.users
    data = parse_json(users.find())
    return {"users": data}
