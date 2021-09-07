import pytesseract
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

def ocr(image):
    custom_oem_psm_config = '--psm 6'

    text = pytesseract.image_to_data(image, lang='eng', config=custom_oem_psm_config)

    confidence_array = []
    full_text = ""

    line_text = text.split("\n")
    for x in line_text[1:]:
        line = x.split("\t")

        # Ignore blank text - where index 11 is blank(empty space).  This is necessary to avoid "IndexError: list index out of range" error
        if len(line) > 11: 
            full_text += line[11] + " "

        confi = int(float(line[10]))
        confidence_array.append(confi)

    average = sum(confidence_array) / len(confidence_array)
    print(text)
    print("AVERAGE CONFIDENCE SCORE:", average)


# call method to output result
ocr(img)

# 1. python3 pre_process_script.py --image images/page17.png
# 2. python3 ocr.py --image temp/image_with_border.jpg