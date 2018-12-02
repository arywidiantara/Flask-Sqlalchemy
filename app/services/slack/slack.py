from config.env import Environment
from flask import request
import requests
import json
import os

class Slack():
    def notification_error(data_error):
        ''' 
            this function for hit slack for notification if something error 
            :data_error class:
            :return object:
        '''
        request_body = request.form
        request_json = request.json
        if request_json != None:
            request_json = json.dumps(request_json)

        if request_body != None:
            request_body = json.dumps(request_body)

        payload = {
            "username": "Flask",
            "channel": "#"+Environment.get_credential('SLACK_CHANNEL'),
            "attachments": [
                {
                    "color": "#2eb886",
                    "author_name": "Environment",
                    "title": Environment.get_credential('APP_ENV'),
                    "text": "New Error",
                    "fields": [
                        {
                            "title": "Error",
                            "value": str(data_error),
                            "short": False,
                        },
                        {
                            "title": "URL",
                            "value": request.url,
                            "short": False,
                        },
                        {
                            "title": "Request URL",
                            "value": json.dumps(request.args),
                            "short": False,
                        },
                        {
                            "title": "Request Body",
                            "value": request_body,
                            "short": False,
                        },
                        {
                            "title": "Request Json",
                            "value": request_json,
                            "short": False,
                        }
                    ]
                }
            ]
        }

        # hit and return data
        return requests.post(
            Environment.get_credential('SLACK_WEBHOOK'),
            data=json.dumps(payload))


        
