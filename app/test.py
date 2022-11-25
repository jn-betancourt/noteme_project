# ====== IMPORT STANDAR LIBRARY FOR TESTING ========
import unittest
# ====== IMPORT MODELS AND DB FOR TESTING =========
from .models import Users
from .mongo_meths import *
from .mongo_conexion import mongo_conexion


class MongoMethsTests(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
