# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
                help="type of preprocessing to be done")
args = vars(ap.parse_args())


# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
    gray = cv2.threshold(gray, 0, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
    gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)


# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file

# image_to_string Returns the result of a Tesseract OCR run on the image to string
# image_to_boxes Returns result containing recognized characters and their box boundaries
# image_to_data Returns result containing box boundaries, confidences, and other information. Requires Tesseract 3.05+. For more information,
# image_to_osd Returns result containing information about orientation and script detection.
# please check the Tesseract TSV documentation

# Example of adding any additional options.
# custom_oem_psm_config = r'--oem 3 --psm 6'
custom_oem_psm_config = ''

text = pytesseract.image_to_string(Image.open(
    filename), lang='eng', config=custom_oem_psm_config)
# text = pytesseract.image_to_osd(Image.open(
    # filename), lang='eng', config=custom_oem_psm_config)
# text = pytesseract.image_to_data(Image.open(
#   filename), lang='eng', config=custom_oem_psm_config)

# os.remove(filename)
print(text)

# Get a searchable PDF
# pdf = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')

# image_to_osd
# show the output images
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
# cv2.waitKey(0)

# Command to run
# python ocr.py --image images/Guardian-1968-06-31.jpg --p blur
# python ocr.py --image images/page_1.jpg --p blur
#
