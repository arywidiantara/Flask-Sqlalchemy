from app.core.json import AlchemyEncoder
import json

class APIController():
    def parse_to_json(model):
        '''
            this function for parse model to json
            :model object:
            :return object:
        '''
        return json.loads(json.dumps(model, cls=AlchemyEncoder))
    