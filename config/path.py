import os

from utilities.path import YamlCustom

yaml = YamlCustom()


def get_path_info():
    return yaml.read_data_from_file(os.getcwd().split('testscripts')[0] + '/resources/config_files/path.yaml')


API_USER_PATH = get_path_info()['api']['user']
API_AUTHENTICATE_PATH = get_path_info()['api']['authenticate']
API_BLOG_PATH = get_path_info()['api']['blog']

API_COCCOC_MUSIC_LISTING = get_path_info()['api']['coccoc_music']['listing']
API_GRAPH_QL_PATH = '/graphql'












