from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from config.app import Config
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"/api/*": {"origins": "*"}})
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

app.config["SQLALCHEMY_DATABASE_URI"] = Config.database()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['SQLALCHEMY_POOL_RECYCLE'] = 299

db = SQLAlchemy(app)

from routes import route
from routes import brand
