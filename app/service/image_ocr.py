
# import the necessary packages
from PIL import Image
import pytesseract
from urllib.request import urlopen
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class Image_Ocr:
    def __init__(self, image_path):
        self.image_path = image_path

    def get_text_and_positions(self):
        custom_oem_psm_config = ''

        try:
            image_file = Image.open(urlopen(self.image_path))
            text = pytesseract.image_to_data(
                image_file, lang='eng', config=custom_oem_psm_config, output_type='dict'
            )
            # print(text['text'])
        except Exception as e:
            return {'error': str(e)}

        # confidence_array = []
        text_array = ' '.join(text['text']).split()
        full_text = ' '.join(text_array)

        return {'full_text': full_text, 'raw_data': text}
        # return {'full_text': full_text, 'confidence': average, 'raw_data': text}

    def get_text_from_image(self):
        custom_oem_psm_config = ''

        try:
            image_file = Image.open(urlopen(self.image_path))
            # image_file = Image.open((self.image_path))
            # text = pytesseract.image_to_string(
            text = pytesseract.image_to_data(
                image_file, lang='eng', config=custom_oem_psm_config
            )
            print(text)
            
        except Exception as e:
            return {'error': str(e)}

        confidence_array = []
        full_text = ""

        line_text = text.split("\n")
        for x in line_text:
            line = x.split("\t")

            # Ignore blank text - where index 11 is blank(empty space).  This is necessary to avoid "IndexError: list index out of range" error
            if len(line) > 11: 
                if line[11] != "text":
                    full_text += line[11] + " "

            if line[10] != '' and line[10] != "conf":
                confi = int(line[10])
                if confi >= 0:
                    confidence_array.append(confi)

        average = sum(confidence_array) / len(confidence_array)
        print(average)

        return {'full_text': full_text, 'confidence': average}

    def get_hOCR(self):
        try:
            pytesseract.pytesseract.run_tesseract(
                self.image_path,
                "output_hocr",extension='jpg',
                lang=None,
                config="--psm 4 -c tessedit_create_hocr=1"
            )

            file = open("output_hocr.hocr", "r") # Location where XML was saved
            h_ocr = file.read()
            file.close()

            return h_ocr

        except Exception as e:
            return {'error': str(e)}


# python get-all-text.py --image 'images/page_1.jpg'
# image-link: https://pbs.twimg.com/media/DzLju9OXQAEhJy0?format=jpg&name=medium
# image-link: https://media1.thehungryjpeg.com/thumbs2/ori_4529_f192d2ef3e2f252ee38a08005d68cd91a73983c9_old-newspapers-digital-paper-textures.jpg