from user import User
from werkzeug.security import safe_str_cmp

users = [
    User(1, 'bob', 'asdf')
]

username_mapping = {u.username: u for u in users}

userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    _user = username_mapping.get(username, None)
    if _user and safe_str_cmp(_user.password, password):
        return _user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
