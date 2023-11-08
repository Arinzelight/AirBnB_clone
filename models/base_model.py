from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    ''' Serve as the base class for other classes'''
    
    def __init__(self, *args, **kwargs):
        '''class constructor for  BaseModel'''
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        '''string representation of the BaseModel instance.'''
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        '''updates 'updated_at' attribute with current datetime'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''dictionary representation of BaseModel instance'''
        base_dict = self.__dict__.copy()
        base_dict['__class__'] = self.__class__.__name__
        base_dict['created_at'] = self.created_at.isoformat()
        base_dict['updated_at'] = self.updated_at.isoformat()
        return base_dict
