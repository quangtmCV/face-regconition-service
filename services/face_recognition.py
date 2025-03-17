from deepface import DeepFace
import numpy as np

def encode_face(image_path):
    # Sử dụng mô hình Facenet để mã hóa khuôn mặt thành vector
    try:
        result = DeepFace.represent(image_path, model_name="Facenet")
        face_encoding = result[0]['embedding']
        return face_encoding
    except Exception as e:
        print("Lỗi khi mã hóa khuôn mặt:", str(e))
        return None
