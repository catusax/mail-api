# -*- coding: utf-8 -*-
# Author: coolrc <root@coolrc.me>
# date:   2021/7/11
""""""

from flask import Flask
from flask import request
from waitress import serve

from conf import config
from mail import MailClient

app = Flask(__name__)
client = MailClient()


@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/send', methods=['GET'])
# def send_simple_mail():
#     to = request.args.get('to', None)
#     if not to:
#         return {'ok': 400, 'msg': 'no receiver!'}
#     subject = request.args.get('sub', None)
#     text = request.args.get('text', None)
#     try:
#         res = client.send_text(receiver=to, subject=subject, text=text)
#         if res:
#             return {'ok': 200, 'msg': ''}
#         else:
#             return {'ok': 500, 'msg': ''}
#     except Exception as e:
#         return {'ok': 500, 'msg': format(e)}


@app.route('/send/'+config['token'], methods=['POST', 'GET'])
def send_text_mail():
    content = request_parse(request)

    try:
        envelop = {
            'receiver': content.get('to', None),
            'cc': content.get('cc', None),
            'bcc': content.get('bcc', None),
            'subject': content.get('sub', None),
            'text': content.get('text', None),
            'html': content.get('html', None)
        }
        if not envelop['receiver']:
            return {'ok': 400, 'msg': 'no receiver!'}

        if not envelop['subject']:
            if not (envelop['text'] or envelop['text']):
                return {'ok': 400, 'msg': 'no content!'}

        res = client.send(**envelop)
        if res:
            return {'ok': 200, 'msg': ''}
        else:
            return {'ok': 500, 'msg': 'unknown error'}
    except Exception as e:
        return {'ok': 500, 'msg': format(e)}


def request_parse(req_data):
    """解析请求数据并以json形式返回"""
    data = {}
    if req_data.method == 'POST':
        data = req_data.json
    elif req_data.method == 'GET':
        data = req_data.args
    return data


if __name__ == '__main__':
    print('running on http://127.0.0.1:8000/')
    serve(app, port=config['http']['port'])
