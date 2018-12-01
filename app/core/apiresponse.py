from flask import jsonify

class APIResponse():

    SUCCESS = 1
    DATA_IS_EMPTY = 2
    ERR_INVALID_LOGIN = 3
    ERR_INVALID_PARAMETER = 4
    ERR_INVALID_ACCESS = 5
    ERR_INVALID_TOKEN = 6
    ERR_VALIDATION = 40
    ERR_NOT_FOUND = 60
    ERR_INVALID_METHOD = 66
    ERR_PROCESS = 88
    ERR_INVALID_KEY = 90
    ERR_SYSTEM = 99

    status = 1
    message = 'Success'
    token = None
    data = {}

    RESPONSE_SUCCESS = 200
    RESPONSE_SUCCESS_NO_CONTENT = 204
    RESPONSE_ERROR_BAD_REQUEST = 400
    RESPONSE_ERROR_UNAUTHORIZED = 401
    RESPONSE_ERROR_FORBIDDEN = 403
    RESPONSE_ERROR_NOT_FOUND = 404
    RESPONSE_ERROR_METHOD_NOT_ALLOWED = 405
    RESPONSE_ERROR_INTERNAL_SERVER_ERROR = 500

    def _message(key):
        '''
            this function for set data message
            :key integer:
            :return string:
        '''
        data =  {
            1: 'Success',
            2: 'Data is Empty',
            3: 'Invalid Login',
            4: 'Invalid Parameters',
            5: 'Access Denied',
            6: 'Invalid Token or token expired',
            40: 'Validation Not Match',
            60: 'Resource not found',
            66: 'Bad Request',
            88: 'Process Failure',
            90: 'API key invalid',
            99: 'Internal system error',
        }

        return data[key]
    
    def SetStatus(key):
        '''
            this function for set status
            :key integer:
        '''
        APIResponse.status = key
        APIResponse.message = APIResponse._message(key)
    
    def GetStatus():
        '''
            this function for get data status
            :return integer:
        '''
        return APIResponse.status
    
    def SetMessage(msg):
        '''
            this function for set data message
            :msg string:
            :return string:
        '''
        APIResponse.message = msg

    def GetMessage():
        '''
            this function for get data message
            :return string:
        '''
        return APIResponse.message 

    def SetToken(value):
        '''
            this function for set data token
            :msg string:
            :return string:
        '''
        APIResponse.token = None
        APIResponse.token = value

    def GetToken():
        '''
            this function for get data token
            :return string:
        '''
        return APIResponse.token

    def SetData(data, key):
        '''
            this function for get data token
            :data object:
            :key string:
        '''
        APIResponse.data = {}

        # set data
        if key != None:
            APIResponse.data[key] = data
        else:
            APIResponse.data = data

    def GetData():
        '''
            this function for get data 
            :return object:
        '''
        return APIResponse.data

    def toArray():
        '''
            this function for return all data
            :return object:
        '''
        # set data
        data = {
            'status': APIResponse.status,
            'message': APIResponse.message,
        }

        # check token value
        if APIResponse.token != None:
            data['token'] = APIResponse.token
        else:
            data['token'] = None

        # check data value
        if APIResponse.data != None:
            data['data'] = APIResponse.data
        else:
            data['data'] = None
        
        # return data
        return jsonify(data)
            
            
