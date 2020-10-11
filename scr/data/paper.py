from mongoengine import Document, StringField, DateTimeField, ListField, IntField, BooleanField
import datetime

class Paper(Document):
    year = StringField(required=True)
    month = StringField(required=True)
    day = StringField(required=True)
    page_number = IntField(required=True)

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

    total_confidence = IntField()
    reviewed_date = DateTimeField()
    reviewed_by = BooleanField()

    # title = StringField()
    # content = StringField()
    # tags = ListField(IntField(required=True))

    meta = {'allow_inheritance': True}
