from mongoengine import Document, StringField, DateTimeField, IntField, EmbeddedDocumentField, ListField, signals
from app.data.papers import Paper
from datetime import datetime
import app.jobs.ocr_image_to_text_job as Ocr
from setup_queue import conn
from rq import Queue, Retry

class File_Import(Document):
    es_index = 'paper_archive'

    year = IntField(required=True)
    month = IntField(required=True, min_value=1, max_value=12)
    day = IntField(required=True, min_value=1, max_value=31)
    page_number = IntField(required=True, min_value=1, unique_with=['year', 'month', 'day'])

    date = DateTimeField()

    file_url = StringField(required=True, unique=True)
    import_date = DateTimeField(default=datetime.utcnow)
    errors = StringField(default='')

    paper = EmbeddedDocumentField(Paper)

    meta = {'allow_inheritance': True}

    @classmethod
    def pre_save(cls, sender, document, **kwargs):
        date_time_str = str(document.year) + '-' + str(document.month) + '-' + str(document.day)
        paper_date = datetime.strptime(date_time_str, '%Y-%m-%d')
        document.date = paper_date.date()

    @classmethod
    def post_save(cls, sender, document, **kwargs):
        if 'created' in kwargs:
            if kwargs['created']:
                q = Queue(connection=conn)
                result = q.enqueue(Ocr.perform_ocr, document.id)



signals.pre_save.connect(File_Import.pre_save, sender=File_Import)
signals.post_save.connect(File_Import.post_save, sender=File_Import)