from mongoengine import EmbeddedDocument, StringField, DateTimeField, ListField, IntField, BooleanField, ObjectIdField
from datetime import datetime

class Paper(EmbeddedDocument):
    import_id = ObjectIdField()
    created_at = DateTimeField(default=datetime.utcnow)

    full_text = StringField(required=True)
    text = ListField(StringField(required=True))
    block_num = ListField(IntField(required=True))
    conf = ListField()
    height = ListField(IntField(required=True))
    left = ListField(IntField(required=True))
    level = ListField(IntField(required=True))
    line_num = ListField(IntField(required=True))
    page_num = ListField(IntField(required=True))
    par_num = ListField(IntField(required=True))
    top = ListField(IntField(required=True))
    width = ListField(IntField(required=True))
    word_num = ListField(IntField(required=True))
    total_confidence = IntField(required=True)
