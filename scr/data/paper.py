from mongoengine import Document, StringField, DateTimeField, ListField, DEFAULT_CONNECTION_NAME
import datetime

class Paper(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True, max_length=200)
    # posted = DateTimeField(default=datetime.datetime.utcnow)
    tags = ListField(StringField(max_length=50))
    meta = {'allow_inheritance': True}
    # meta = {
    #   "db_alias": "newspaper",
    #   'collection': 'paper'
    # }