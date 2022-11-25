from pymongo import MongoClient
import certifi


ca = certifi.where()


def mongo_conexion(uri):

    notes_db = None
    try:
        client = MongoClient(uri)
        local_db = client.local
        notes_db = local_db.Notes
    except ConnectionError as e:
        print(f"conexion error {e}")

    return notes_db
