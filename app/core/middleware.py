from flask import g, request, redirect, url_for, make_response
from app.exceptions.handler import ExceptionHandler
from app.core.apiresponse import APIResponse
from app.core.request import request_data
from functools import wraps
from app import cache
import os

@cache.cached(timeout=30, key_prefix="app_key")
def app_key(f):
    '''
        this function for middleware data key
        :f object:
        :return object:
    '''
    @wraps(f)
    
    # set object for data asynchronous data
    def decorated_function(*args, **kwargs):
        # check header
        app_key = request.headers.get('app-key')

        # get data request
        if app_key == None:
            app_key = request_data('app-key')

        # check key
        if app_key != os.environ.get('APP_KEY'):
            errors = ExceptionHandler.key_wrong()
            APIResponse.SetStatus(APIResponse.ERR_INVALID_KEY)
            APIResponse.SetData(errors, 'errors')
            return make_response(APIResponse.toArray(), APIResponse.RESPONSE_ERROR_UNAUTHORIZED)
        else:
            return f(*args, **kwargs)

    # return object
    return decorated_function
