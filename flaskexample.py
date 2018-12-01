from os.path import join, dirname
from dotenv import load_dotenv
import os

# Load File Environments
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# from app import app
from app import app

if __name__ == '__main__':
    env = os.environ.get('APP_ENV', 'local')
    if env != "local":
        app.run(host='0.0.0.0')
    else:           
        # check main 
        host = os.environ.get('APP_HOST', '127.0.0.1')
        port = os.environ.get('APP_PORT', '2800')
        debug = os.getenv('APP_DEBUG', 'True')
        app.run(host, port, debug)
