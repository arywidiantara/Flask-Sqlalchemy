from config.env import Environment
from flask import request
import datetime
import hashlib
import random
import string
import time
import re
import os

class Helper():
    def get_full_media(folder_name, file_name):
        '''
            this function for get data from s3 data
            :folder_name string:
            :file_name string:
            :object string:
        '''
        if file_name == None or file_name == "":
            return request.host_url + "medias/default.jpg"
            
        if Environment.get_credential('FILESYSTEM_DRIVER') == 's3':
            image = "https://" + Environment.get_credential(
                'AWS_BUCKET') + ".s3.amazonaws.com/" + folder_name + file_name
        else:
            image = request.host_url + "public/" + folder_name + file_name

        # return image
        return image
    
    def get_extention(filename):
        '''
            this function get extension file
            :filename string:
            :return string:
        '''
        return filename.split('.')[-1]
    
    def hashmd5(name):
        '''
            this function hash string to md5
            :name string:
            :return string:
        '''
        name_encode = name.encode("utf-8")
        hash_data = hashlib.md5(name_encode)
        return hash_data.hexdigest()

    def now():
        '''
            this for get current date
            :return datetime:
        '''
        ts = time.time()
        # return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        return datetime.datetime.fromtimestamp(ts)

    def now_string():
        '''
            this for get current date
            :return datetime:
        '''
        ts = time.time()
        return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    def today():
        '''
            this for get current date
            :return datetime:
        '''
        ts = time.time()
        return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

    def randomword(length):
        '''
            this function for get string random
            :length integer:
            :return string:
        '''
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return ''.join(random.choice(letters) for i in range(length))

    def date(key):
        '''
            this function for get data for the future or pass
            :key integer:
            :return datetime:
        '''
        return datetime.datetime.now() + datetime.timedelta(key)

    def get_list_ids(values):
        '''
            this get all id base on list data
            :values array:
            :return array:
        '''
        ids = []
        for value in values:
            if value not in ids:
                # append data
                ids.append(value.id)    
        
        # return data
        return ids

    def pagination(model):
        '''
            this function helper for define data for pagination
            :model object:
            :return object:
        '''
        return {
            'has_next_page': model.has_next,
            'has_prev_page': model.has_prev,
            'total_data': model.total,
        }

    def create_folder(directory):
        '''
            this function for create folder on local
            :directory string:
        '''
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        return None

    def slugify(s):
        '''
            Simplifies ugly strings into something URL-friendly.
            :s string:
            :return string:
        '''

        # "[Some] _ Article's Title--"
        # "[some] _ article's title--"
        s = s.lower()

        # "[some] _ article's_title--"
        # "[some]___article's_title__"
        for c in [' ', '-', '.', '/']:
            s = s.replace(c, '_')

        # "[some]___article's_title__"
        # "some___articles_title__"
        s = re.sub('\W', '', s)

        # "some___articles_title__"
        # "some   articles title  "
        s = s.replace('_', ' ')

        # "some   articles title  "
        # "some articles title "
        s = re.sub('\s+', ' ', s)

        # "some articles title "
        # "some articles title"
        s = s.strip()

        # "some articles title"
        # "some-articles-title"
        s = s.replace(' ', '-')

        return s
