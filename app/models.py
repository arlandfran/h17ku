from flask_login import UserMixin
from app import login_manager, mongo


class User(UserMixin):
    def __init__(self, email, username, pwd_hash):
        self.email = email
        self.username = username
        self.pwd_hash = pwd_hash

    def get_id(self):
        return self.username


@login_manager.user_loader
def load_user(username):
    username_exists = mongo.db.users.find_one({"username": username})
    if username_exists:
        user = User(
            email=username_exists["email"],
            username=username,
            pwd_hash=username_exists["pwd_hash"],
        )
        return user
    return None
