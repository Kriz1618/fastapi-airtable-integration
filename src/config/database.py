import os

from pymongo import MongoClient

DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_HOST = os.environ['DB_HOST']
CLUSTER = os.environ['CLUSTER']

try:
    connection = MongoClient(DB_HOST, username='DB_USER',
                             password=DB_PASSWORD, serverSelectionTimeoutMS=5000)
    print(' DB conected successfully '.center(50, '*'))
except Exception as err:
    print('Error connecting to the DB server: {}'.format(err))


def getCluster():
    db = None
    try:
        db = connection[CLUSTER]
        return db
    except Exception as err:
        print('Error connecting to the cluster {}: {}'.format(CLUSTER, err))
