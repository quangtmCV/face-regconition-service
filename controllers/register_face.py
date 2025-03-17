from flask import request, jsonify
from services.face_recognition import encode_face
from models.user_model import save_user
import os

def register_face():
    if 'image' not in request.files or 'name' not in request.form:
        return jsonify({"error": "Thiếu ảnh hoặc tên"}), 400

    image = request.files['image']
    name = request.form['name']

    # Lưu ảnh tạm thời
    if not os.path.exists('temp'):
        os.makedirs('temp')
    image_path = f"./temp/{image.filename}"
    image.save(image_path)

    # Mã hóa khuôn mặt
    face_encoding = encode_face(image_path)
    if face_encoding is None:
        return jsonify({"error": "Không thể nhận diện khuôn mặt"}), 500

    # Lưu vào MongoDB
    user_id = save_user(name, face_encoding)
    os.remove(image_path)

    return jsonify({"message": "Đăng ký thành công", "user_id": user_id}), 201
