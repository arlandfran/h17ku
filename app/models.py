from flask_login import UserMixin
from app import login_manager, mongo


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
