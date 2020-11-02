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
    raw_text = []
    height = []
    top = []
    width = []
    left = []
    confidence = []

    for index, text in enumerate(ocr_text['raw_data']['text'], start=0):
        striped_text = text.strip()
        if striped_text:
            full_text += (striped_text + ' ')
            raw_text.append(striped_text)
            height.append(ocr_text['raw_data']['height'][index])
            top.append(ocr_text['raw_data']['top'][index])
            width.append(ocr_text['raw_data']['width'][index])
            left.append(ocr_text['raw_data']['left'][index])
            confi = int(ocr_text['raw_data']['conf'][index])
            if confi >= 0:
                confidence.append(confi)

    ocr_text['raw_data']['full_text'] = full_text
    ocr_text['raw_data']['total_confidence'] =  sum(confidence) / len(confidence)

    document.update(set__paper=ocr_text['raw_data'])

    document.reload()
    payload = {'full_text': document.paper.full_text, 'page': document.page_number, 'file_url': document.file_url, 'date': document.date, 'raw_text': raw_text, 'height': height, 'top': top, 'width': width, "left": left  }

    es.index(index=document.es_index, id=document.id, body=payload)
