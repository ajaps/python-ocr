# python-ocr

## README

## Dependencies

- tesseract 5.0.0-beta
- Python3
- pytesseract
- opencv
- Flask

## Configuration

- Install dependencies

  Install redis server
  ```
   brew install redis
  ```

  Install ElasticSearch 7.13(ES)
  https://www.elastic.co/guide/en/elasticsearch/reference/current/brew.html
  ```
    brew tap elastic/tap
    brew install elastic/tap/elasticsearch-full
  ```

  Install MongoDB @4.2
  https://docs.mongodb.com/v4.2/tutorial/install-mongodb-on-os-x/
  ```
    brew tap mongodb/brew
    brew install mongodb-community@4.2
  ```

  Install Redis
  ```
    brew install redis
  ```

 Install python dependant libraries located in requirements.txt
  ```
   pip3 install -r requirements.txt
  ```
  
- Add Installed dependency to requirements.txt
  ```
   pip3 freeze | grep -i mongoengine >> requirements.txt
  ```
- Install foreman
  ```
   gem install foreman
  ```

- Create ES mapping
  ```
    curl -X PUT "localhost:9200/paper_archive?pretty" -H 'Content-Type: application/json' -d'
    {
      "mappings": {
        "properties" : {
          "full_text": {
            "type": "text",
            "fields": {
              "keyword": {
                "type": "keyword",
                "ignore_above": 256
              }
            }
          },
          "file_url": { "type": "keyword"},
          "date": {
            "type": "date"
          },
          "page": { "type": "integer" },
          "raw_text": { "type": "keyword" },
          "conf": { "type": "long" },
          "height": { "type": "integer" },
          "left": { "type": "integer" },
          "top": { "type": "integer" },
          "width": { "type": "integer" }
        }
      },
      "settings": {}
    }
    '
  ```
## Local Development

- Run `foreman start` in your terminal
- load POST http://localhost:5000/ocr-image?image_url=https://media1.thehungryjpeg.com/thumbs2/ori_4529_f192d2ef3e2f252ee38a08005d68cd91a73983c9_old-newspapers-digital-paper-textures.jpg
- load GET http://localhost:5000/ocr-image?image_url=https://media1.thehungryjpeg.com/thumbs2/ori_4529_f192d2ef3e2f252ee38a08005d68cd91a73983c9_old-newspapers-digital-paper-textures.jpg to return xml identifying page structure
- Search for text in documents  GET http://localhost:5000/search?query=Subscription rato months rat 
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
http://localhost:5000/search?text=Subscription rato months rat 