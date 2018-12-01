import os

class Environment():
    def get_credential(key):
        '''
            this function for get credential environment
            :key string:
            :return string:
        '''
        param = {
            'APP_LOC': os.getenv('APP_LOC'),
            'FILESYSTEM_DRIVER': os.getenv('FILESYSTEM_DRIVER'),
            'AWS_ACCESS_KEY': os.getenv('AWS_ACCESS_KEY'),
            'AWS_ACCESS_SECRET': os.getenv('AWS_ACCESS_SECRET'),
            'AWS_REGION': os.getenv('AWS_REGION'),
            'AWS_BUCKET': os.getenv('AWS_BUCKET'),
            'BRIGHTCOVE_AUTH_ENDPOINT': os.getenv('BRIGHTCOVE_AUTH_ENDPOINT'),
            'BRIGHTCOVE_INGEST_ENDPOINT': os.getenv('BRIGHTCOVE_INGEST_ENDPOINT'),
            'BRIGHTCOVE_ENDPOINT': os.getenv('BRIGHTCOVE_ENDPOINT'),
            'BRIGHTCOVE_REGION': os.getenv('BRIGHTCOVE_REGION'),
            'BRIGHTCOVE_API_KEY': os.getenv('BRIGHTCOVE_API_KEY'),
            'BRIGHTCOVE_ACCOUNT_ID': os.getenv('BRIGHTCOVE_ACCOUNT_ID'),
            'BRIGHTCOVE_CLIENT_ID': os.getenv('BRIGHTCOVE_CLIENT_ID'),
            'BRIGHTCOVE_CLIENT_SECRET': os.getenv('BRIGHTCOVE_CLIENT_SECRET'),
        }

        # check if not empty
        if key not in param:
            return None

        # return key
        return param[key]
        
