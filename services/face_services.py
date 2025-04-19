import os
import uuid
from embeddings.extractor import *
from embeddings_database.database import Database
from scipy.spatial.distance import cosine
from PIL import Image

class FaceService:
    def __init__(self):
        self.base_dir = "data/faces"
        os.makedirs(self.base_dir, exist_ok=True)

    def recognize_image(image_path):
        # Khởi tạo các đối tượng cần thiết
        extractor = EmbeddingExtractor()
        db = Database()

        # Trích xuất vector nhúng từ ảnh cần nhận diện
        new_image_embedding = extractor.extract_embedding(image_path)

        # Lấy tất cả các vector nhúng từ database
        all_embeddings = db.get_all_embeddings()
        print(f"Found {len(all_embeddings)} embeddings in the database.")

        # Biến lưu trữ kết quả ảnh giống nhất
        min_distance = float('inf')
        best_match = None

        # Duyệt qua tất cả các vector nhúng trong database và so sánh với vector của ảnh mới
        for db_image_path, db_label, db_embedding in all_embeddings:
            distance = cosine(new_image_embedding, db_embedding)
            print(distance)# Tính Cosine Distance
            if distance < min_distance:  # Tìm ảnh có khoảng cách nhỏ nhất
                min_distance = distance
                best_match = (db_label, db_image_path)

        # Đóng kết nối database
        db.close()

        # Kiểm tra kết quả
        if min_distance < 0.5:  # Ngưỡng khoảng cách để coi là ảnh giống nhau (có thể điều chỉnh)
            return best_match
        else:
            return None

    def register(self, name, image_file):
        user_dir = os.path.join(self.base_dir, name)
        if os.path.exists(user_dir):
            return {'error': 'User already exists'}

        os.makedirs(user_dir)
        image_path = os.path.join(user_dir, f'{uuid.uuid4()}.jpg')
        image_file.save(image_path)

        return {'message': 'Face registered successfully'}

    def add_face(self, name, image_file):
        user_dir = os.path.join(self.base_dir, name)
        if not os.path.exists(user_dir):
            return {'error': 'User does not exist'}

        image_path = os.path.join(user_dir, f'{uuid.uuid4()}.jpg')
        image_file.save(image_path)

        return {'message': 'Face added successfully'}

    def save_image_to_sub_dir(self, image, sub_image_dir):
        try:
            image_name = image.filename
            # Define the full path to save the image
            image_path = os.path.join(sub_image_dir, image_name)

            # Save the image
            image.save(image_path)
            return image_path
        except Exception as e:
            pass
            return str(e)
