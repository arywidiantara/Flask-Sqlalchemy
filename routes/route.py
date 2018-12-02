from flask import make_response, render_template, jsonify, send_from_directory
from app.repositories.slackrepository import SlackRepository
from app.exceptions.handler import ExceptionHandler
from app.core.apiresponse import APIResponse
from config.env import Environment
from app import app, cache
import os

@app.route('/', methods=['GET'])
def index():
    return '<html><body><h1 align="center">Flask Example</h1></body></html>'

@app.route('/medias/<path:path>')
def send_medias(path):
    return send_from_directory(Environment.get_credential('APP_LOC') + "/medias", path)

@app.route('/public/<path:path>')
def send_public(path):
    return send_from_directory(Environment.get_credential('APP_LOC') +"/public", path)

@app.errorhandler(404)
def page_not_found(error):
    '''
    return data page not found
        :error class: 
        :return json: 
    '''
    environment = Environment.get_credential('APP_ENV')
    # check environment
    if environment != "local":
        errors = ExceptionHandler.message_error()
        APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
        APIResponse.SetData(errors, 'errors')
        return make_response(APIResponse.toArray(), APIResponse.RESPONSE_ERROR_NOT_FOUND)
    else:
        return error

@app.errorhandler(405)
def method_not_allowed(error):
    '''
    return data method not allowed
        :error class: 
        :return json: 
    '''
    environment = Environment.get_credential('APP_ENV')
    # check environment
    if environment != "local":
        APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
        APIResponse.SetData(['Method Not Allowed'], 'errors')
        return make_response(APIResponse.toArray(), APIResponse.RESPONSE_ERROR_METHOD_NOT_ALLOWED)
    else:
        return error

@app.errorhandler(Exception)
def internal_server_error(error):
    '''
    return data internal server error
        :error class: 
        :return json: 
    '''
    environment = Environment.get_credential('APP_ENV')
    # check environment
    if environment != "local":
        SlackRepository.send_data_slack(error)
        errors = ExceptionHandler.message_error()
        APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
        APIResponse.SetData(errors, 'errors')
        return make_response(APIResponse.toArray(), APIResponse.RESPONSE_ERROR_INTERNAL_SERVER_ERROR)
    else:
        return jsonify(error=str(error)), 500
