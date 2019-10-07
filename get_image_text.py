
# import the necessary packages
from PIL import Image
import pytesseract
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

class Image_Ocr:
    def __init__(self, image_path):
        self.image_path = image_path

    def get_text_from_image(self):
        custom_oem_psm_config = ''

        try:
            image_file = Image.open(urlopen(self.image_path))
            text = pytesseract.image_to_string(
                image_file, lang='eng', config=custom_oem_psm_config
            )
        except Exception as e:
            return {'error': e.message}

        return {'data': text}

# python get-all-text.py --image 'images/page_1.jpg'
