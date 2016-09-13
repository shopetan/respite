#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

from app import RESPUIT
import argparse
import jinja2

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', help='ポート番号', type=int)
    args = parser.parse_args()
    select_port = args.port

    respuit = RESPUIT(__name__)
    respuit.routes()
    respuit.config['JSON_AS_ASCII'] = False

    respuit.run(host='0.0.0.0', debug=True, port=select_port)
