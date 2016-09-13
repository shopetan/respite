from flask_restful import Resource, reqparse
from flask import request, jsonify
from app import ASG
import json,urllib3,requests
import re

class ChatBot(Resource):

    def post(self):

        get_percolate_url = "http://localhost:9200/zexy/logs/_percolate"
        get_answer_url = "http://localhost:9200/zexy/logs/_search"
        
        json_data = request.get_json(force=True)
        query = json_data['query']

        
        get_percolate_payload = {"highlight":{"fields":{"question":{"pre_tags":["("],"post_tags":[")"]}}},"size":100,"doc":{"question":query}}

        r_get = requests.get(get_percolate_url, data=json.dumps(get_percolate_payload))
        data = r_get.json()
        
        percolate = {}
        delete = {ord(u'('): None,ord(u')'): None}
        old_question_len = 0
        new_question_len = 0

        for question in data['matches']:
            match = re.findall(r'\(.+?\)',question['highlight']['question'][0])
            new_question_len = len(match)

            if new_question_len > old_question_len:
                old_question_len = new_question_len
                new_question_len = 0
                word_array = []
                for word in match:
                    word_array.append({"term":{"question":word.translate(delete)}})
                percolate.update({'cluster_id':question['_id'], 'question_words':word_array})

        get_answer_payload = {"fields":["cluster_id","category","question","answer","master_answer"],"query":{"bool":{"must":{"term":{"cluster_id":percolate['cluster_id']}},"minimum_should_match":1,"should":percolate['question_words']}}}

        r_get = requests.get(get_answer_url, data=json.dumps(get_answer_payload))
        data = r_get.json()

        return jsonify(data['hits']['hits'][0]['fields'])
