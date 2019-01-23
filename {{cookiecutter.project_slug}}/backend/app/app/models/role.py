from mongoengine import Document
from mongoengine.fields import StringField


class Role(Document):
    meta = {'collection': 'roles'}
    name = StringField(max_length=255, unique=True)
    description = StringField(max_length=255)

    def __unicode__(self):
        return self.name
