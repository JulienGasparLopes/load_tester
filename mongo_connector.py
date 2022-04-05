from pymongo import MongoClient
from helpers import load_secrets


class MongoConnector:
    def __init__(self, db_name) -> None:
        secrets = load_secrets()
        uri = f"mongodb+srv://{secrets['mongoUrl']}?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
        client = MongoClient(
            uri,
            tls=True,
            tlsCertificateKeyFile="./mongo_certificate.pem"
        )
        self._db_name = db_name
        self._db = client[db_name]

    def find_documents(self, collection_name, filter=None):
        return self._db[collection_name].find(filter)

    def insert_documents(self, collection_name, documents):
        self._db[collection_name].insert_many(documents)
