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

# CSV Erode image
img = cv2.imread(args["image"], 0)
kernel = np.ones((2, 2), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, erosion)

# Example of adding any additional options.
# custom_oem_psm_config = r'--oem 3 --psm 6'
# custom_oem_psm_config = "-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
custom_oem_psm_config = ''

text = pytesseract.image_to_string(Image.open(
    filename), lang='eng', config=custom_oem_psm_config)
# config = "-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# os.remove(filename)
print(text)

# python erode_image.py - -image images/page_1.jpg
