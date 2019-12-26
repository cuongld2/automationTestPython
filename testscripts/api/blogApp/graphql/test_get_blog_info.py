import json

from pytest_testrail.plugin import pytestrail

from api.blog.graphql.blogs import Blogs
from api.blog.rest.user import User
from utilities.database import RestAPIDatabase
from utilities.random_utils import RandomGenerator


class TestGetBlogsInfo:
    user_api = User()
    restapi_query = RestAPIDatabase()
    random_gen = RandomGenerator()
    blog_graphql_api = Blogs()

    @pytestrail.case('C8')
    def test_get_all_blog_id_and_contents_with_count(self, set_up_mysql):
        username = self.random_gen.random_string(8) + '@gmail.com'
        query = """
        {
            blogs(count:1){
                            id,
                            content
                            }
        }
        """
        try:
            response = self.user_api.create_new_user_data_class(username, 'Abcd12345$', 'Le Dinh Cuong')
            assert 200 == response.status_code
            response = self.user_api.authen_user_login(username, 'Abcd12345$')
            assert response.status_code == 200
            token_object = json.loads(response.text)
            assert token_object['token'] is not None
            response_blog = self.blog_graphql_api.get_blog_info(query, token_object['token'])
            print(response_blog)
            assert response_blog['data']['blogs'][0]['id'] == 1
            if 'title' in response_blog['data']['blogs'][0]:
                raise print('Content existed in response')
            assert 'title' not in str(response_blog)
        finally:
            self.restapi_query.delete_user_info_by_username(set_up_mysql, username)