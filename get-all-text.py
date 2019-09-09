# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
                help="type of preprocessing to be done")
args = vars(ap.parse_args())

custom_oem_psm_config = ''

text = pytesseract.image_to_string(Image.open(
    args["image"]), lang='eng', config=custom_oem_psm_config)

print(text)
