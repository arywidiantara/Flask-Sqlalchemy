from app.helpers.helper import Helper
from config.env import Environment
from config.path import Path
from io import BytesIO
from PIL import Image
import pandas as pd
import botocore
import base64
import boto3
import os

class Storage():
    def upload(filename, filename_base64, config_path):
        '''
            this function upload image and save image
            :filename string:
            :filename_base64 string:
            :config_path string:
            :return object:
        '''
        if Environment.get_credential('FILESYSTEM_DRIVER') == 's3':
            directory = Path.pathmedia(config_path)
            directory_local = Path.fullpathmedia(config_path)
            ext = Helper.get_extention(filename)
            image = Storage.upload_local(filename, filename_base64, config_path)
            Storage.upload_s3(directory_local+filename,
                              directory+filename, "image/"+ext)
            Storage.remove_file(directory_local+filename)
        else:
           image = Storage.upload_local(filename, filename_base64, config_path)
        
        return image
    
    def upload_local(filename, filename_base64, config_path):
        '''
            this function  save image on local
            :filename string:
            :filename_base64 string:
            :config_path string:
            :return object:
        '''
        directory = Path.fullpathmedia(config_path)

        # create folder on local
        Helper.create_folder(directory)
            
        image = None
        try:
            starter = filename_base64.find(',')
            image_data = filename_base64[starter+1:]
            image_data = bytes(image_data, 'utf8')
            image = Image.open(BytesIO(base64.b64decode(image_data)))
            image.save(directory + filename)
        except Exception as e:
                print("Something Happened In Image: ", e)

        return image

    def upload_s3(file_directory_local, file_directory, content_type):
        '''
            this function upload data s3
            :file_directory_local string:
            :file_directory string:
            :content_type string:
            :return object:
        '''
        s3 = boto3.client(
            Environment.get_credential('FILESYSTEM_DRIVER'),
            aws_access_key_id=Environment.get_credential('AWS_ACCESS_KEY'),
            aws_secret_access_key=Environment.get_credential(
                'AWS_ACCESS_SECRET')
        )
        try:
            s3.upload_file(
                file_directory_local,
                Environment.get_credential('AWS_BUCKET'),
                file_directory,
                ExtraArgs={
                    "ACL": "public-read",
                    "ContentType": content_type,
                }
            )
        except Exception as e:
            print("Something Happened: ", e)
            return None

    def remove_file(filename):
        '''
            this function delete image on local
            :filename string:
        '''
        os.remove(filename)