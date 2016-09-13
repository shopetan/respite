from flask_restful import Resource, reqparse
from flask import request, jsonify
from config import Config
from app import RESPUIT
import json,urllib3,requests
import re

class HotPepper(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('lat', type=float)
        self.parser.add_argument('lng', type=float)
        self.parser.add_argument('range', type=int)
        self.args = self.parser.parse_args()
        
    def get(self,lat=None, lng=None, range=None):
        get_hotpepper_url = "http://webservice.recruit.co.jp/hotpepper/gourmet/v1/?"
        API_KEY = Config.API_KEY

        key = "key=" + API_KEY
    
        get_hotpepper_url = get_hotpepper_url + key + "&lat=" + str(self.args['lat']) + "&lng=" + str(self.args['lng']) + "&range=" + str(self.args['range']) + "&format=json"
        
        # get_hotpepper_url = "https://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=171fc38efdf97244&lat=34.67&lng=135.52&range=5&order=4&format=json"
        
        r_get = requests.get(get_hotpepper_url)
        data = r_get.json()
        
        return jsonify(data)
