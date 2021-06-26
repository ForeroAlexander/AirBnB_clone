#!/usr/bin/python3

from datetime import datetime
import uuid
import models


class BaseModel:
    def __init__(self, *args, **Kwargs):
        """Args:
        id: id of instance
        create_at: time of creation
        update_at: time of creation or modification
        """
        if not Kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.update_at = datetime.now()
            models.storage.new(self)
        else:
            for attr_name, attr in Kwargs.items():
                if attr_name == "created_at" or attr_name == "update_at":
                    attr = datetime.strptime(attr, "%Y-%m-%dT%H:%M:%S.%f")
                if attr_name != "__class__":
                    setattr(self, attr_name, attr)


    def __str__(self):
        """"return str representation"""
        return "[{}] ({}) {}".format(str(type(self).__name__), self.id,
                                     str(self.__dict__))

    def __repr__(self):
        """return object representation"""
        return "[{}] ({}) {}".format(str(type(self).__name__), self.id,
                                            str(self.__dict__))

    def save(self):
        """updates the update_at attr w/ current datetime"""
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary representation of __dict__
        w/ __class__ added"""
        d = dict(**self.__dict__)
        d['__class__'] = str(type(self).__name__)
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
