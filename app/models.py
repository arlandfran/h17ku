from flask_login import UserMixin
from marshmallow import Schema, fields

from app import login_manager, mongo


class NewUserSchema(Schema):
    email = fields.Email(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    password2 = fields.String(required=True)


class User(UserMixin):
    def __init__(self, email, username):
        self.email = email
        self.username = username

    def get_id(self):
        return self.username


@login_manager.user_loader
def load_user(username):
    username_exists = mongo.db.users.find_one({"username": username})
    if username_exists:
        user = User(
            email=username_exists["email"],
            username=username,
        )
        return user
    return None
