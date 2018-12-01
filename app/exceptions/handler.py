
class ExceptionHandler():
    def wrong_extension(key):
        '''
            this function return wrong extension
            :return array:
        '''
        return [ExceptionHandler.extension_wrong(key)]

    def multiple_wrong_extension(datas):
        '''
            for handling mulitiple validation required data
            :datas array:
            :return array:
        '''
        all_data = []
        for data in datas:
            # return data in apped
            all_data.append(ExceptionHandler.extension_wrong(data))

        # return data
        return all_data

    def extension_wrong(key):
        '''
            this function return wrong extension
            :return array:
        '''
        key = key.replace("_", " ")
        key = key.replace("-", " ")
        return 'Extension %s is Encorrectly Formatted' % (key)

    def key_wrong():
        '''
            this function return key wrong
            :return array:
        '''
        return ['Invalid Key']

    def access_denied():
        '''
            this function return access denied
            :return array:
        '''
        return ['Your dont have access for the page']

    def multiple_validation_required(datas):
        '''
            for handling mulitiple validation required data
            :datas array:
            :return array:
        '''
        all_data = []
        for data in datas:
            # return data in apped
            all_data.append(ExceptionHandler.required(data))
        
        # return data
        return all_data

    def message_error():
        '''
            handling error if environment staging or production
            :return array:
        '''   
        return ['We are facing some technical difficulties. Please try again later.']

    def wrong_format(key):
        '''
            handling return validation wrong format
            :key string:
            :return array:
        '''   
        key = key.replace("_", " ")
        key = key.replace("-", " ")
        return ['Your %s is Encorrectly Formatted' % (key)]

    def validation_exist(key):
        '''
            handling return validation exist
            :key string:
            :return array:
        '''   
        key = key.replace("_", " ")
        key = key.replace("-", " ")
        return ['Your %s is Not Exist' % (key)]

    def already_exist(key):
        '''
            handling return the data exist
            :key string:
            :return array:
        '''   
        key = key.replace("_", " ")
        key = key.replace("-", " ")
        return ['Your %s is Already Exist' % (key)]

    def required(key):
        '''
            handling return data required
            :key string:
            :return array:
        '''
        key = key.replace("_", " ")
        key = key.replace("-", " ")
        return '%s is Required' % (key)

    def validation_required(key):
        '''
            handling return validation required
            :key string:
            :return array:
        '''
        return [ExceptionHandler.required(key)]

    def validation_exists(key):
        '''
            handling return validation not found
            :key string:
            :return array:
        '''
        key = key.replace("_", " ")
        key = key.replace("-", " ")
        return ['%s is Not Found' % (key)]

    def validation_exist_two_param(key1, key2):
        '''
            handling return validation multiple params
            :key1 string:
            :key2 string:
            :return array:
        '''
        key1 = key1.replace("_", " ")
        key1 = key1.replace("-", " ")
        key2 = key2.replace("_", " ")
        key2 = key2.replace("-", " ")
        return ['%s is Not Found At %s' % (key1, key2)]
