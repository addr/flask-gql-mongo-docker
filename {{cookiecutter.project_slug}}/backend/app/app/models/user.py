from mongoengine import Document
from mongoengine.fields import (StringField, EmailField, ListField,
                                ReferenceField, BooleanField)


class User(Document):
    meta = {'collection': 'users'}
    first_name = StringField(max_length=255)
    last_name = StringField(max_length=255)
    email = EmailField(unique=True)
    roles = ListField(ReferenceField('Role'))
    password = StringField(max_length=255)
    active = BooleanField()

    def __unicode__(self):
        return "{first_name} {last_name}".format(
            first_name=self.first_name, last_name=self.last_name)
