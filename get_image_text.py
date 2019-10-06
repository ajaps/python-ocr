
# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import numpy as np

class Image_Ocr:
  def __init__(self, image_path):
    self.image_path = image_path

  def get_text_from_image(self):
    custom_oem_psm_config = ''
    text = pytesseract.image_to_string(
      Image.open(self.image_path), lang='eng', config=custom_oem_psm_config
    )

    return text

# python get-all-text.py --image 'images/page_1.jpg'
