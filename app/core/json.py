from sqlalchemy.ext.declarative import DeclarativeMeta
from datetime import timedelta
import datetime
import json

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        '''
            this function for generate from sqlalchemy to json
            :obj object:
            :return json:
        '''
        if isinstance(obj, bytes):
            return None
            
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                if field not in self.not_include():
                    data = obj.__getattribute__(field)

                    # check type data if date time
                    if isinstance(data, datetime.datetime):
                        data = str(data)

                    # check type data if date time
                    if isinstance(data, timedelta):
                        data = str(data)

                    try:
                        json.dumps(data) # this will fail on non-encodable values, like other classes
                        fields[field] = data
                    except TypeError:
                        fields[field] = None
            # a json-encodable dict
            return fields
        
        return json.JSONEncoder.default(self, obj)
    
    def not_include(self):
        '''
            this function for not included global object not return
            :return array:
        '''
        return [
            'save',
            'delete',
            'first',
            'get_all',
            ]
