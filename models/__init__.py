#!/usr/bin/python3
"""This Instantiates a storage object.

from models.city import City
from models.amenity import Amenity
from models.place import Place
from os import environ
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
