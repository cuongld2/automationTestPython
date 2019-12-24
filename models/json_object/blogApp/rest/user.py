from typing import Optional


def userinfo(username, password, fullname):
    return {
        'username': username,
        'password': password,
        'fullname': fullname
    }


class UserInfo(object):
    id: Optional[int]
    username: str
    password: str
    fullname: str

    def __init__(self, username, password, fullname):
        self.username = username
        self.password = password
        self.fullname = fullname











