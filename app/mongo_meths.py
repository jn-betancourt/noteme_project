# ======== MONGODB STANDART LIBRARY ==================
from bson.objectid import ObjectId
from . import db_mongo
# ========== UNIQUES ID CREATION ==================
import random
import string


# ========== CREATION ID ====================
number_of_strings = 5
length_of_string = 8
id_note = ''
for x in range(number_of_strings):
    id_note = 'n'+''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(length_of_string))


# ========= CRUD METHODS FOR MONGODB ================
def insert_new_doc(email):

    doc = {
        "email": email,
        "notes": []
    }

    id_doc = db_mongo.insert_one(doc).inserted_id

    return id_doc


def retrieve_notes(id_doc):

    notes = db_mongo.find_one({"_id": ObjectId(id_doc)})

    return notes


def insert_new_note(id_doc, **kwargs):

    db_mongo.update_one(
                        {"_id": ObjectId(id_doc)},
                        {"$push": 
                                {"notes": 
                                    {"id_note": id_note, 
                                    "title": kwargs['kwargs']['title'], 
                                    'description': kwargs['kwargs']['description']}}})


def modify_doc(id_doc, new_doc):
 
    db_mongo.replace_one({"_id": ObjectId(id_doc)}, new_doc)
