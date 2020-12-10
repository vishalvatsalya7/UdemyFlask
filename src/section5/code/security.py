from user import User
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    _user = User.find_by_username(username)
    if _user and safe_str_cmp(_user.password, password):
        return _user


def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)
