from app.modules.brand.adapter import BrandAdapter
from app.core.apicontroller import APIController
from app.helpers.helper import Helper
from app.core.storage import Storage
from config.app import Config
from config.path import Path

class BrandRepository():
    def get_all_brands(query_filter):
        '''
            this function for get list brands 
            :query_filter object:
            :return object:
        '''
        # get data brand
        brands = BrandAdapter.get_all_brands(query_filter)
        # make json format
        all_datas = []
        for brand in brands:
            data_brand = APIController.parse_to_json(brand)
            data_brand['image_url'] = Helper.get_full_media(
                Path.pathmedia('brand_image'), brand.logo)
            all_datas.append(data_brand)

        # return data
        return {
            'brands': all_datas,
        }

    def get_brands(query_filter):
        '''
            this function for get all data brands 
            :query_filter object:
            :return object:
        '''
        return BrandAdapter.get_all_brands(query_filter)

    def get_id_first(id):
        '''
            this function for get data Brand base on id first
            :id string:
            :return object:
        '''
        return BrandAdapter.brand_id_first(id)
    
    def get_list_pagination(page, query_filter):
        '''
            this function for get list brands base on pagination
            :page integer:
            :return object:
        '''
        # get data brand
        brands = BrandAdapter.get_list_pagination(
            page, Config.per_page(), query_filter)

        # mapping data pagination
        pagination = Helper.pagination(brands)

        # get data brand
        data_brands = brands.items
        print(data_brands)
        
        # make json format
        all_datas = []
        for brand in data_brands:
            print("data")
            print(brand)
            data_brand = APIController.parse_to_json(brand)
            print(data_brand)
            data_brand['image_url'] = Helper.get_full_media(
                Path.pathmedia('brand_image'), brand.logo)
            all_datas.append(data_brand)
        
        # return data
        return {
            'pagination': pagination,
            'brands': all_datas,
        }

    def create_or_update(param):
        '''
            this function for save or update data brand
            :param object:
            :return object:
        '''
        if param['logo'] != None and param['logo_base64'] != None:
            Storage.upload(param['logo'], param['logo_base64'],'brand_image')

        if param['id'] == None:
            return BrandAdapter.create_data(param)
            
        else:
            return BrandAdapter.update_data(param)

    def delete_brand(id):
        '''
            this function for delete data brand
            :id integer:
        '''
        BrandAdapter.delete_data(id)
    