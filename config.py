from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "as_face_recognition_for_android_app"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
