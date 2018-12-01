from flask import request

def request_data(key):
    '''
        get data request from body and header
        :key string:
        :return string:
    '''
    # get data from header
    request_data = request.args.get(key)

    # check data if not null and return the data
    if request_data != None:
        return request_data
    else:
        # check data from body request
        f = request.form
        if key not in f.keys():
            request_json_kyes = request.json
            if request_json_kyes != None:    
                if key not in request_json_kyes.keys():
                    return None
                else:
                    # get data from body request
                    data_json = request.json[key]
                    if not data_json:
                        return None
                    else:
                        return data_json
            else:
                return None
        else:
            # get data from body request
            data = request.form[key]
            if not data:
                return None
            else:
                return data
        