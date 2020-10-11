from app.service.image_ocr import Image_Ocr
import app.data.imports as model
from app.data import mongo_db
from app.infrastructure.setup_elasticsearch import es

def perform_ocr(document_id):
    print('OCRing Document with ID: ' + str(document_id))

    document = model.File_Import.objects(id=document_id).first()

    Ocr_Engine = Image_Ocr(document.file_url)
    ocr_text = Ocr_Engine.get_text_and_positions()

    full_text = ""
    for x in ocr_text['raw_data']['text']:
        if x.strip():
            full_text += (x + ' ')

    ocr_text['raw_data']['full_text'] = full_text

    # es.index(index='paper_archieve', id=1, body=ocr_text['raw_data'])
    es.index(index='paper_archieve', id=2, body={'text': "AJOAPSHFGJ fdbshjg"})

    document.update(set__paper=ocr_text['raw_data'])
