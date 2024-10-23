import psycopg2
import os

class Config(object):
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
  
    #SQLite3:

    '''BASE_DIR =  os.path.abspath(os.path.dirname(__file__))
    DB_URI = "sqlite:///" + os.path.join(BASE_DIR, "database.db")'''

    #MySQL:
    '''DB_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username="", password="", hostname="", databasename="")'''

    #PostgreSQL:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://{username}:{password}@{hostname}/{databasename}".format(username="curso", password="J05huarg#", hostname="localhost", databasename="curso")