from os import error
from flask_login import UserMixin
from marshmallow import Schema, fields, validate

from app import login_manager, mongo


class NewUserSchema(Schema):
    email = fields.Email(required=True)
    username = fields.String(
        required=True,
        validate=validate.Length(min=4, error="username must be at least 4 characters"),
    )
    password = fields.String(
        required=True,
        validate=validate.Length(min=8, error="password must be at least 8 characters"),
    )
    password2 = fields.String(
        required=True,
        validate=validate.Length(
            min=8,
            error="password must be at least 8 characters",
        ),
    )


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
