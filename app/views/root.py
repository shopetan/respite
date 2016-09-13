from flask_restful import Resource, reqparse
from flask import request, jsonify, render_template
from app import ASG
import json,urllib3,requests
import re

class Root(Resource):
    def get(self):
        
        message = 'aaa'
        title = 'bbb'
        
        return render_template("./index.html",
                               message=message, title=title)
