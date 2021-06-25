#!/usr/bin/python3
"""
create a unique FileStorage istance
for you application
"""
from models.engine.file_storage import FileStorage

Storage = FileStorage()
Storage.reload()
