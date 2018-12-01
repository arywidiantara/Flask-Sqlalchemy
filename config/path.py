from config.env import Environment

class Path():
    def pathmedia(key):
        '''
            this function for get path image
            :key string:
            :return string:
        '''
        param = {
            'brand_image': 'flask-example/brand/image/',
        }

        # check if not empty
        if key not in param:
            return None

        # return key
        return param[key]

    def fullpathmedia(key):
        '''
            this function for get path image
            :key string:
            :return string:
        '''
        path = Path.pathmedia(key)

        if path == None:
            return None

        return Environment.get_credential('APP_LOC')+"/public/"+path
