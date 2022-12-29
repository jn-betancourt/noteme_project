# ====== IMPORT STANDAR FOR TESTING ===========
import unittest
import mockupdb
# ====== IMPORT APP FLASK =============
from .. import create_app, db
from ..models import Users
from ..mongo_conexion import mongo_conexion
from ..mongo_meths import *


class BaseTestClass(unittest.TestCase):

    def setUp(self) -> None:
        self.app = create_app("config.testing")
        self.client = self.app.test_client()

        self.server = mockupdb.MockupDB(auto_ismaster={"maxWireVersion": 3})
        self.server.run()

        self.mongo_db = mongo_conexion(self.server.uri)
        print(self.server.uri)

        with self.app.app_context():
            db.create_all()


    
    def tearDown(self) -> None:
        self.server.stop()
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
