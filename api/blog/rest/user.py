import json

import requests

from config.environment import API_SERVER_URL
from config.path import API_USER_PATH
from models.json_object.blogApp.rest.user import userinfo, UserInfo


class User:

    def create_new_user(self, username, password, fullname):
        return requests.post(API_SERVER_URL + API_USER_PATH, data=json.dumps(userinfo(username, password, fullname)),
                             headers={'Content-Type': 'application/json'}
                             )

    def create_new_user_data_class(self, username, password, fullname):
        user_info_instance = UserInfo(username, password, fullname)
        s = json.dumps(user_info_instance.__dict__)
        return requests.post(API_SERVER_URL + API_USER_PATH, data=s, headers={'Content-Type': 'application/json'})

