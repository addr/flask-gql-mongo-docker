from mongoengine import Document
from mongoengine.fields import (StringField, EmailField, ListField,
                                ReferenceField, BooleanField)
from app.core.security import verify_password


class User(Document):
    meta = {'collection': 'users'}
    first_name = StringField(max_length=255)
    last_name = StringField(max_length=255)
    email = EmailField(unique=True)
    roles = ListField(ReferenceField('Role'))
    password = StringField(max_length=255)
    active = BooleanField()

    def authenticate_user(self, password):
        if not verify_password(password, self.password):
            return False

    def __unicode__(self):
        return "{first_name} {last_name}".format(
            first_name=self.first_name, last_name=self.last_name)
