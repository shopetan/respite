import os

class Config(object):

    RESTFUL_JSON = { 'ensure_ascii': False }
    API_KEY = os.environ.get('HOT_PEPPER_API')
