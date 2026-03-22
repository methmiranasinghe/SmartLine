from pymongo import MongoClient
from app.config import MONGODB_URL, DATABASE_NAME

client = MongoClient(MONGODB_URL)
db = client[DATABASE_NAME]

users_collection = db["users"]
services_collection = db["services"]
appointments_collection = db["appointments"]
queue_collection = db["queue"]