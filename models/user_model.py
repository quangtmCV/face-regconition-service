from config import db
import datetime

def save_user(name, face_encoding):
    user = {
        "name": name,
        "face_encoding": face_encoding,
        "created_at": datetime.datetime.utcnow()
    }
    result = db.users.insert_one(user)
    return str(result.inserted_id)