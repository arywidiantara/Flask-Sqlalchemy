from app.core.apicontroller import APIController
from app.core.request import request_data
from io import BytesIO
from PIL import Image
import base64

class Validation():
    def required(datas):
        '''
            this function for validation required data
            :datas array:
            :return array:
        '''
        required = []
        for data in datas:
            data_request = request_data(data)
            # check data request is empty
            if data_request == None:
                required.append(data)
        
        # return data
        return required

    def int(datas):
        '''
            this function for validation data int data
            :datas array:
            :return array:
        '''
        data_int = []
        for data in datas:
            try:
                data_request = int(request_data(data))
            except:
                # check data request is not int
                data_int.append(data)

        # return data
        return data_int

    def float(datas):
        '''
            this function for validation data float data
            :datas array:
            :return array:
        '''
        data_float = []
        for data in datas:
            try:
                float(request_data(data))
            except:
                # check data request is not float
                data_float.append(data)

        # return data
        return data_float

    def base64(datas):
        '''
            this function for validation data base64 data
            :datas array:
            :return array:
        '''
        data_base64 = []
        for filename_base64 in datas:
            try:
                starter = filename_base64.find(',')
                image_data = filename_base64[starter+1:]
                image_data = bytes(image_data, 'utf8')
                image = Image.open(BytesIO(base64.b64decode(image_data)))
            except:
                # check data request is not base64
                data_base64.append(filename_base64)

        # return data
        return data_base64

    def validateExtension(filename, extensions):
        # '''
        #     this function for validation extension
        #     :filename string:
        #     :extensions array:
        #     :return boolean:
        # '''
    	return '.' in filename and filename.split('.')[-1] in extensions
