import os
from mongoengine import connect, disconnect
from dotenv import load_dotenv

load_dotenv()

disconnect()
connect(alias='default', host=os.getenv("MONGO_DB_HOST"))
