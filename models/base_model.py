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
        if Kwargs:
            
            for key, value in Kwargs.items():
                if key == "created_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())  # unique id
            self.created_at = datetime.now()  # datetime when is created
            self.updated_at = datetime.now()  # date when is updated
            models.storage.new(self)



    def __str__(self):
        """  this function prints __str__ method """
        """" pep8 check"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

    def save(self):
        """ updates with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary representation of __dict__
        w/ __class__ added"""
        '''returns a dictionary with all keys/value of the instance'''
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy

