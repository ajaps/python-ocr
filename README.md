# python-ocr

## README

## Dependencies

- Python3
- pytesseract
- opencv
- Flask

## Configuration

- Install dependencies

  ```
   pip3 install -r requirements.txt
  ```
  
- Add Installed dependency to requirements.txt
  ```
   pip3 freeze | grep -i mongoengine >> requirements.txt
  ```

## Local Development

- Run `python3 ocr_api.py` in your terminal
- load POST http://localhost:5000/ocr-image?image_url=https://media1.thehungryjpeg.com/thumbs2/ori_4529_f192d2ef3e2f252ee38a08005d68cd91a73983c9_old-newspapers-digital-paper-textures.jpg
- load GET http://localhost:5000/ocr-image?image_url=https://media1.thehungryjpeg.com/thumbs2/ori_4529_f192d2ef3e2f252ee38a08005d68cd91a73983c9_old-newspapers-digital-paper-textures.jpg to return xml identifying page structure

## Testing

- N/A

- Run the tests

  ```
  
  ```

## Deployment

N/A

## API Documentation
 - N/A


## Limitations
 - run POST http://localhost:5000/ocr-image?image_url=https://i.pinimg.com/originals/d3/8b/9d/d38b9dce1010a9c46fc29b39b3d5bede.jpg
 This errors out with a message `IndexError: list index out of range`
