#!/usr/bin/python3
"""
BaseModel module
"""
import uuid
import datetime


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Object initialiser
        """
        from models import storage
        if kwargs:
            for k, v in kwargs.items():
                if k in ("created_at", "updated_at"):
                    self.__dict__[k] = datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                elif k == "__class__":
                    continue
                else:
                    self.__dict__[k] = v
        
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        storage.new(self)

    def __str__(self):
        """
        Prints the string representation of the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates when the object is modified
        """
        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the object
        """
        dict = {}
        dict["__class__"] = self.__class__.__name__

        for k, v in self.__dict__.items():
            if isinstance(v, datetime.datetime):
                v = v.isoformat()
                dict[k] = v

            dict[k] = v

        return dict
