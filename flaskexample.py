from config.env import Environment
from os.path import join, dirname
from dotenv import load_dotenv

# Load File Environments
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# from app import app
from app import app

if __name__ == '__main__':
    env = Environment.get_credential('APP_ENV')
    if env != "local":
        app.run(host='0.0.0.0')
    else:           
        # check main 
        host=Environment.get_credential('APP_HOST')
        port=Environment.get_credential('APP_PORT')
        debug=Environment.get_credential('APP_DEBUG')
        app.run(host, port, debug)
