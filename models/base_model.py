#!/usr/bin/python3
'''
BaseModel - Base Class
'''

import uuid
from datetime import datetime, date, time
import models


class BaseModel():
    ''' BaseModel - attributes and methods'''

    __nb_objects = 0

    def __init__(self, *args, **kwargs):
        '''__init__ - attributes'''
        if len(kwargs) != 0:
            at_integers = ['my_integers', 'number_rooms', 'number_bathrooms',
                           'max_guest', 'price_by_night', 'my_number']
            at_floats = ['latitude', 'longitude']
            at_datetime = ['created_at', 'updated_at']
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in at_integers:
                        setattr(self, key, int(value))
                    elif key in at_floats:
                        setattr(self, key, float(value))
                    elif key in at_datetime:
                        if key == 'created_at':
                            self.created_at = datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f')
                        if key == 'updated_at':
                            self.updated_at = datetime.strptime(
                                value, '%Y-%m-%dT%H:%M:%S.%f')
                    else:
                        setattr(self, key, value)
            models.storage.new(self)
        else:
            BaseModel.__nb_objects += 1
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''__str__ - print instance'''
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__))

    def save(self):
        '''save - save changes of instance'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''to_dict - dictionary of the instance'''
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        return(new_dict)
