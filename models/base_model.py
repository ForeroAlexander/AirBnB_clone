#!/usr/bin/python3

from datetime import datetime
import uuid
import models


class BaseModel:
    def __init__(self *args, **Kwargs):
        """Args:
        id: id of instance
        create_at: time of creation
        update_at: time of creation or modification
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.update_at = datetime.now()
            models.storage.new(self)

        else:


    def __str__(self):
        """"return str representation"""


    def __repr__(self):
        """return obkect representation"""

    def save(self):
        """updates the update_at attr w/ current datetime"""

    def to_dict(self):
        """returns a dictionary representation of __dict__
        w/ __class__ added"""
