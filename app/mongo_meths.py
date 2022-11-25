# ======= IMPORT STANDAR MONGO DB =============
from . import db_mongo
from bson.objectid import ObjectId


def insert_new_doc(email, id_note, title="", description=""):

    doc = {
        "email": email,
        "notes": [
            {"id_note": id_note, "title": title, "description": description},
        ]
    }

    id_inserted = db_mongo.insert_one(doc).inserted_id
    return id_inserted


def retrieve_notes(id_doc):

    notes = db_mongo.find({"_id": ObjectId(id_doc)})

    return notes
    

def delete_note(id_doc, id_note):

    db_mongo.update_one({
            "_id": ObjectId(id_doc),
            "notes": [
                {"id_note": id_note}
            ]},
            {"$unset":
                {
                    "id_note": "",
                    "title": "",
                    "description": ""
                }
             })


def update_content(id_doc, id_note, **kargs):

    db_mongo.update_one({"_id": id_doc, "notes": [{"id_note": id_note}]}, **kargs)
