import os

class Environment():
    def get_credential(key):
        '''
            this function for get credential environment
            :key string:
            :return string:
        '''
        param = {
            'APP_ENV': os.environ.get('APP_ENV'),
            'APP_KEY': os.environ.get('APP_KEY'),
            'APP_TIMEZONE': os.environ.get('APP_TIMEZONE'),
            'APP_HOST': os.environ.get('APP_HOST'),
            'APP_PORT': os.environ.get('APP_PORT'),
            'APP_DEBUG': os.environ.get('APP_DEBUG'),
            'APP_LOC': os.environ.get('APP_LOC'),
            'DB_CONNECTION': os.getenv('DB_CONNECTION'),
            'DB_HOST': os.getenv('DB_HOST'),
            'DB_PORT': os.getenv('DB_PORT'),
            'DB_DATABASE': os.getenv('DB_DATABASE'),
            'DB_USERNAME': os.getenv('DB_USERNAME'),
            'DB_PASSWORD': os.getenv('DB_PASSWORD'),
            'SLACK_WEBHOOK': os.getenv('SLACK_WEBHOOK'),
            'SLACK_CHANNEL': os.getenv('SLACK_CHANNEL'),
            'FILESYSTEM_DRIVER': os.getenv('FILESYSTEM_DRIVER'),
            'AWS_ACCESS_KEY': os.getenv('AWS_ACCESS_KEY'),
            'AWS_ACCESS_SECRET': os.getenv('AWS_ACCESS_SECRET'),
            'AWS_REGION': os.getenv('AWS_REGION'),
            'AWS_BUCKET': os.getenv('AWS_BUCKET'),
        }

        # check if not empty
        if key not in param:
            return None

        # return key
        return param[key]
        
