from pymongo import MongoClient
from redis import Redis
from rq import Queue

from os import environ

# env variables
PHP = environ.get('PHPSESSID')
token = '/?token=%s' % environ.get('API_TOKEN')

# mongodb
db = MongoClient()

# redis queue
q = Queue(connection=Redis())
