from models.user import UserModel
from werkzeug.security import safe_str_cmp


def authenticate(username, password):
    _user = UserModel.find_by_username(username)
    if _user and safe_str_cmp(_user.password, password):
        return _user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
