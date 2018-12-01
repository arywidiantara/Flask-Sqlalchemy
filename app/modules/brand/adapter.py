from sqlalchemy.sql.expression import func
from app.helpers.helper import Helper
from app.models.brand import Brand
from app import db

class BrandAdapter():
    def get_brands():
        '''
            this function for get data brands
            :return query:
        '''
        return db.session.query(Brand).filter(Brand.deleted_at == None)
    
    def brand_query(brands, query_filter):
        '''
            this function for query data brands
            :brands object:
            :query_filter object:
            :return query:
        '''
        # check brand name
        if 'name' in query_filter:
            if query_filter['name'] != None:
                brands = brands.filter(Brand.name.like(
                    "%" + query_filter['name'] + "%"))

        # check slug
        if 'slug' in query_filter:
            if query_filter['slug'] != None:
                brands = brands.filter(
                    Brand.slug == query_filter['slug'])

        # check brand id
        if 'brand_id' in query_filter:
            if query_filter['brand_id'] != None:
                brands = brands.filter(
                    Brand.id != query_filter['brand_id'])

        # check start date
        if 'start_date' in query_filter:
            if query_filter['start_date'] != None:
                brands = brands.filter(
                    Brand.created_at >= query_filter['start_date'])

        # check end date
        if 'end_date' in query_filter:
            if query_filter['end_date'] != None:
                brands = brands.filter(
                    Brand.created_at <= query_filter['end_date'])

        # check data order by
        if 'order_by' in query_filter:
            if query_filter['order_by'] == "name":
                brands = brands.order_by(Brand.name.desc())
            else:
                brands = brands.order_by(Brand.id.desc())
        else:
            brands = brands.order_by(Brand.id.desc())

        # return data
        return brands

    def get_all_brands(query_filter):
        '''
            this function for get list Brands 
            :page integer:
            :perpage integer:
            :return object:
        '''
        # get brands and filter 
        brands = BrandAdapter.get_brands()
        brands = BrandAdapter.brand_query(brands, query_filter)
        
        # return all data brands
        return brands.all()

    def brand_id_first(id):
        '''
            this function for get data brand base on id first
            :id integer:
            :return object:
        '''
        brands = BrandAdapter.get_brands()
        return brands.filter(Brand.id == id).first()
    
    def get_list_pagination(page, perpage, query_filter):
        '''
            this function for get list Brands base on pagination
            :page integer:
            :perpage integer:
            :return object:
        '''
        # get brands and filter
        brands = BrandAdapter.get_brands()
        brands = BrandAdapter.brand_query(brands, query_filter)

        return brands.paginate(page, perpage, error_out=False)

    def update_data(param):
        '''
            this function for update data brand
            :param array:
            :return object:
        '''
        brand = BrandAdapter.brand_id_first(param['id'])
        brand.name = param['name']
        brand.description = param['description']

        if param['logo'] != None:
            brand.logo = param['logo']
            
        brand.slug = param['slug']
        brand.updated_at = Helper.now()
        brand.save()

        # return data brans
        return brand
    
    def create_data(param):
        '''
            create data brand
            :param object:
            :return object:
        '''
        data_brand = Brand(name = param['name'],
                description = param['description'],
                logo = param['logo'],
                slug = param['slug'],
                created_at = Helper.now(),
                updated_at = Helper.now())
        data_brand.save()

        #return data
        return data_brand

    def delete_data(id):
        '''
            this function for delete data brand
            :id integer:
            :user_id integer:
        '''
        brand = BrandAdapter.brand_id_first(id)
        brand.deleted_at = Helper.now()
        brand.save()
