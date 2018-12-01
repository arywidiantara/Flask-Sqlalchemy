from app.core.request import request_data
import os

class Config():
    def database():
        ''' 
            Configuration For Database 
            :return string:
        '''
        connection = os.environ.get('DB_CONNECTION')
        username = os.getenv('DB_USERNAME')
        password = os.getenv('DB_PASSWORD')
        host = os.getenv('DB_HOST')
        port = os.environ.get('DB_PORT')
        database = os.getenv('DB_DATABASE')

        # mysql://username:password@server/db
        SQLALCHEMY_DATABASE_URI = connection + "://" + \
            username + ":" + password + "@" + host + ":" + port + "/" + database
        
        return SQLALCHEMY_DATABASE_URI

    def database_analytic():
        ''' 
            Configuration For Database Analytics 
            :return string:
        '''
        connection = os.environ.get('ANALYTIC_DB_CONNECTION')
        username = os.getenv('ANALYTIC_DB_USERNAME')
        password = os.getenv('ANALYTIC_DB_PASSWORD')
        host = os.getenv('ANALYTIC_DB_HOST')
        port = os.environ.get('ANALYTIC_DB_PORT')
        database = os.getenv('ANALYTIC_DB_DATABASE')

        # mysql://username:password@server/db
        SQLALCHEMY_DATABASE_URI = connection + "://" + \
            username + ":" + password + "@" + host + ":" + port + "/" + database

        return SQLALCHEMY_DATABASE_URI
    
    def per_page():
        '''
            this function for create default data perpage
            :return integer:
        '''
        perpage = request_data('per_page')
        if perpage == None:
            perpage = 15
        else:
            perpage = int(perpage)
        return perpage
