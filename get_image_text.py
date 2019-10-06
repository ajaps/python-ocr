
# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import numpy as np
import io
from urllib.request import urlopen


class Image_Ocr:
    def __init__(self, image_path):
        self.image_path = image_path

    def get_text_from_image(self):
        custom_oem_psm_config = ''

        try:
            fd = urlopen(self.image_path).read()
            image_file = io.BytesIO(fd)

            text = pytesseract.image_to_string(
                Image.open(image_file), lang='eng', config=custom_oem_psm_config
            )
        except Exception as e:
            return {'error': e.message}

        return {'data': text}

# python get-all-text.py --image 'images/page_1.jpg'
