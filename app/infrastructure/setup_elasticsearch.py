import os
from elasticsearch import Elasticsearch

es_url = os.getenv('ELASTICSEARCH_URL', 'http://localhost:9200')
es = Elasticsearch(es_url)

# CREATE MAPPINGS VIA CONSOLE(curl)
    # curl -X PUT "localhost:9200/paper_archive?pretty" -H 'Content-Type: application/json' -d'
    # {
    #   "mappings": {
    #     "properties" : {
    #       "full_text": {
    #         "type": "text",
    #         "fields": {
    #           "keyword": {
    #             "type": "keyword",
    #             "ignore_above": 256
    #           }
    #         }
    #       },
    #       "file_url": { "type": "keyword"},
    #       "date": {
    #         "type": "date"
    #       },
    #       "page": { "type": "integer" },
    #       "raw_text": { "type": "keyword" },
    #       "conf": { "type": "long" },
    #       "height": { "type": "integer" },
    #       "left": { "type": "integer" },
    #       "top": { "type": "integer" },
    #       "width": { "type": "integer" }
    #     }
    #   },
    #   "settings": {}
    # }
    # '