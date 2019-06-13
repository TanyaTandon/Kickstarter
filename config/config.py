
import os 
MODE='AWS'
LOGGING_CONFIG =  "config/logging_local.conf"
DEBUG = True
SOURCE_BUCKET = 'bossbucket'

PORT = 9033
APP_NAME = "dear-genie"

SQLALCHEMY_TRACK_MODIFICATIONS = True
HOST = "127.0.0.1"

conn_type = "mysql+pymysql"
user = os.environ.get("MYSQL_USER")
password = os.environ.get("MYSQL_PASSWORD")
host = os.environ.get("MYSQL_HOST")
port = os.environ.get("MYSQL_PORT")
db_name = 'msia423'
if MODE == 'AWS':
    SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}:{}/{}".\
    format(conn_type, user, password, host, port, db_name)
else:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../database/msia423.db'


#Logging
LOGGER_NAME = 'root'

PATH_TO_MODEL = "models/GradientBoosting.pkl"
