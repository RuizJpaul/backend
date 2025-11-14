from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
mongo_client = MongoClient(os.getenv("MONGO_URI"))
mongo_db = mongo_client["tutor_ia"]
