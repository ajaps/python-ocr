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

    document.update(set__paper=ocr_text['raw_data'])

    document.reload()
    payload = {'full_text': document.paper.full_text, 'page': document.page_number, 'file': document.file_url, 'date': document.date}

    es.index(index=document.es_index, id=document.id, body=payload)
