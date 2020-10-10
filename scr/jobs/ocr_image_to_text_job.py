from scr.service.image_ocr import Image_Ocr
import scr.data.imports as model
from scr.data import mongo_db

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