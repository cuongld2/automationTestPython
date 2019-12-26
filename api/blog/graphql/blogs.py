import requests

from config.environment import API_SERVER_URL
from config.path import API_GRAPH_QL_PATH


class Blogs:

    def get_blog_info(self, query, token):
        request = requests.post(API_SERVER_URL + API_GRAPH_QL_PATH, json={'query': query}, headers={"Authorization": f"Bearer {token}"})
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))
