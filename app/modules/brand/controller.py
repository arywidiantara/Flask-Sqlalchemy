from app.modules.brand.repository import BrandRepository
from app.core.apicontroller import APIController
from app.core.request import request_data
from app.helpers.helper import Helper
from flask import request

class BrandController():
    def get_all_brands():
        '''
            this function for get list brand 
            :return object:
        '''
        query_filter = {
            'name': request_data('name'),
            'order_by': request_data('order_by'),
            'start_date': request_data('start_date'),
            'end_date': request_data('end_date'),
        }
        return BrandRepository.get_all_brands(query_filter)

    def get_list_pagination():
        '''
            this function for get list brand base on pagination
            :return object:
        '''
        query_filter = {
            'name': request_data('name'),
            'order_by': request_data('order_by'),
            'start_date': request_data('start_date'),
            'end_date': request_data('end_date'),
        }
        return BrandRepository.get_list_pagination(request.args.get('page', 1, type=int), query_filter)

    def detail_brand():
        '''
            this function for get brand first
            :return object:
        '''
        return BrandRepository.get_id_first(request_data('id'))
        
    def create_update_brand():
        '''
            this function for create and update data brand
            :return object:
        '''
        logo = request_data('logo')
        if logo != None:
            logo_ext = "."+Helper.get_extention(request_data('logo'))
            logo_hash = Helper.hashmd5(Helper.randomword(
                20) + Helper.now_string()+logo_ext)
            logo = Helper.randomword(10) +logo_hash + logo_ext
        param = {
            'id': request_data('id'),
            'name': request_data('name'),
            'description': request_data('description'),
            'logo': logo,
            'logo_base64': request_data('logo_base64'),
            'slug': Helper.slugify(request_data('name')),
        }
        return BrandRepository.create_or_update(param)

    def delete_brand():
        '''
            this function for delete brand
            :return object:
        '''
        BrandRepository.delete_brand(request_data('id'))
        
