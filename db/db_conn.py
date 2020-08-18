from sqlalchemy import create_engine
from decouple import config

# load environment variables
DB_USER = config("DB_USER")
DB_PASS = config("DB_PASS")
DB_NAME = config("DB_NAME")
DB_PORT = config("DB_PORT")
DB_IP = config("DB_IP")


def connect_db():
    # create db create_engine
    db = create_engine(f'postgresql://{DB_USER}:{DB_PASS}@{DB_IP}:{DB_PORT}/{DB_NAME}')
    return db