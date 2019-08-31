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

# CSV Dillate image
img = cv2.imread(args["image"], 0)
kernel = np.ones((5, 5), np.uint8)
dilate = cv2.dilate(img, kernel, iterations=1)

filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, dilate)
