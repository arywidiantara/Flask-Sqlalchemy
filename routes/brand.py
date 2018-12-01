from app.modules.brand.controller import BrandController
from app.modules.brand.repository import BrandRepository
from app.exceptions.handler import ExceptionHandler
from app.core.apicontroller import APIController
from app.core.apiresponse import APIResponse
from app.core.validation import Validation
from app.core.request import request_data
from app.core.middleware import app_key
from app.helpers.helper import Helper
from config.extension import Ext
from flask import make_response
from config.path import Path
from app import app

@app.route('/api/v1/brands', methods=['GET'])
@app_key
def get_all_brands():
    '''
        this function for get list brands
        :return object:
    '''
    # validation name
    name = request_data('name')
    if name != None:
        if len(name) < 3:
            APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
            APIResponse.SetData(['Your name minimum 3 characters'], 'errors')
            return make_response(APIResponse.toArray(), APIResponse.RESPONSE_ERROR_BAD_REQUEST)
            
    # get data brand
    brands = BrandController.get_all_brands()

    # return data
    APIResponse.SetStatus(APIResponse.SUCCESS)
    APIResponse.SetData(brands, None)
    return make_response(APIResponse.toArray(), APIResponse.RESPONSE_SUCCESS)

@app.route('/api/v1/brand/paginations', methods=['GET'])
@app_key


def get_brands():
    '''
        this function for get list brand base on pagination
        :return object:
    '''
    # get data brand
    brands = BrandController.get_list_pagination()

    # return data
    APIResponse.SetStatus(APIResponse.SUCCESS)
    APIResponse.SetData(brands, None)
    return make_response(APIResponse.toArray(), APIResponse.RESPONSE_SUCCESS)

@app.route('/api/v1/brand/detail', methods=['GET'])
@app_key
def get_detail_brand():
    '''
        this function for get detail brand
        :return object:
    '''
    # get data brand
    brand = BrandController.detail_brand()
    # check brand is not null
    if brand == None:            
        errors = ExceptionHandler.validation_exists("brand_id")
        APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
        APIResponse.SetData(errors, 'errors')
        return make_response(APIResponse.toArray())

    # parse data to json
    data_brand = APIController.parse_to_json(brand)
    data_brand['image_url'] = Helper.get_full_media(
        Path.pathmedia('brand_image'), brand.logo)

    # return data
    APIResponse.SetStatus(APIResponse.SUCCESS)
    APIResponse.SetData(data_brand, 'brand')
    return make_response(APIResponse.toArray(), APIResponse.RESPONSE_SUCCESS)

@app.route('/api/v1/brand/form', methods=['POST','PUT'])
@app_key
def form_brand():
    '''
        this function for create and update data brand
        :return object:
    '''
    # set validation required
    validations = Validation.required(['name','description'])
    if len(validations) > 0:
        errors = ExceptionHandler.multiple_validation_required(validations)
        APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
        APIResponse.SetData(errors, 'errors')
        return make_response(APIResponse.toArray(), APIResponse.RESPONSE_ERROR_BAD_REQUEST)

    # check id is not null
    if request_data('id') != None:
        # get data brand
        brand = BrandController.detail_brand()
        # check brand is not null
        if brand == None:            
            errors = ExceptionHandler.validation_exists("brand_id")
            APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
            APIResponse.SetData(errors, 'errors')
            return make_response(APIResponse.toArray())
        
        # validation image
        if request_data('logo') != None and request_data('logo_base64') == None:
            errors = ExceptionHandler.validation_required("logo_base64")
            APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
            APIResponse.SetData(errors, 'errors')
            return make_response(APIResponse.toArray())
        if request_data('logo') == None and request_data('logo_base64') != None:
            errors = ExceptionHandler.validation_required("logo")
            APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
            APIResponse.SetData(errors, 'errors')
            return make_response(APIResponse.toArray())

        query_filter = {
            'brand_id': request_data('id'),
            'slug': Helper.slugify(request_data('name')),
        }
        brand_data = BrandRepository.get_brands(query_filter)
        if len(brand_data) > 0:
            errors = ExceptionHandler.already_exist("brand_name")
            APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
            APIResponse.SetData(errors, 'errors')
            return make_response(APIResponse.toArray(), APIResponse.RESPONSE_ERROR_BAD_REQUEST)
    else:
        # set validation required
        validations = Validation.required(
            ['logo','logo_base64'])
        if len(validations) > 0:
            errors = ExceptionHandler.multiple_validation_required(validations)
            APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
            APIResponse.SetData(errors, 'errors')
            return make_response(APIResponse.toArray(), APIResponse.RESPONSE_ERROR_BAD_REQUEST)

        query_filter = {
            'slug': Helper.slugify(request_data('name')),
        }
        brand_data = BrandRepository.get_brands(query_filter)
        if len(brand_data) > 0:
            errors = ExceptionHandler.already_exist("brand_name")
            APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
            APIResponse.SetData(errors, 'errors')
            return make_response(APIResponse.toArray(), APIResponse.RESPONSE_ERROR_BAD_REQUEST)

    # set validation mime
    if request_data('logo') != None:
        validation_mime = Validation.validateExtension(
            request_data('logo'), Ext.image())
        if validation_mime == False:
            errors = ExceptionHandler.wrong_extension("logo")
            APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
            APIResponse.SetData(errors, 'errors')
            return make_response(APIResponse.toArray())

    # update data brand
    brand = BrandController.create_update_brand()
    
    # parse data to json
    data_brand = APIController.parse_to_json(brand)
    data_brand['image_url'] = Helper.get_full_media(
        Path.pathmedia('brand_image'), brand.logo)
    
    # return data
    APIResponse.SetStatus(APIResponse.SUCCESS)
    APIResponse.SetData(data_brand, 'brand')
    return make_response(APIResponse.toArray(), APIResponse.RESPONSE_SUCCESS)

@app.route('/api/v1/brand/delete', methods=['DELETE'])
@app_key
def delete_brand():
    '''
        this function for delete brand
        :return object:
    '''
    # set    required
    validations = Validation.required(['id'])
    if len(validations) > 0:
        errors = ExceptionHandler.multiple_validation_required(validations)
        APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
        APIResponse.SetData(errors, 'errors')
        return make_response(APIResponse.toArray(), APIResponse.RESPONSE_ERROR_BAD_REQUEST)

    # check id is not null
    if request_data('id') != None:
        # get data group brand
        brand = BrandController.detail_brand()
        
        if brand == None:            
            errors = ExceptionHandler.validation_exists("brand_id")
            APIResponse.SetStatus(APIResponse.ERR_INVALID_PARAMETER)
            APIResponse.SetData(errors, 'errors')
            return make_response(APIResponse.toArray())

    # get data group brand
    BrandController.delete_brand()
    
    # return data for 204
    resp = make_response()
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp, APIResponse.RESPONSE_SUCCESS_NO_CONTENT
