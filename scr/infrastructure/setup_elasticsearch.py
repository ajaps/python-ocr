import os
from elasticsearch import Elasticsearch

es_url = os.getenv('ELASTICSEARCH_URL', 'http://localhost:9200')
es = Elasticsearch(es_url)

# print(es_url)
# es.index(index='my_index', id=1, body={'text': 'this is a test'})