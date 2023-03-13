from django.db import models
from abc import ABC, abstractclassmethod
from app.models import Post

# Create your models here.
class TagBase(ABC):
    @abstractclassmethod
    def get_ids(cls, tag):
        '''
        get the match objects that has the same tag
        '''
    @abstractclassmethod
    def get_class_name(cls):
        '''
        get the match objects that has the same tag
        '''

class PostsTag(TagBase):
    base_class = Post

    @classmethod
    def get_ids(cls, tag):
        return list(cls.base_class.objects.filter(tags__name=tag).values('id'))
    
    @classmethod
    def get_class_name(cls)-> str:
        return cls.base_class.__name__