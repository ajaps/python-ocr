from mongoengine import connect, disconnect
import os

from dotenv import load_dotenv

load_dotenv()

disconnect()
connect(alias='default', host=os.getenv("MONGO_DB_HOST"))
