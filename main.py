# main.py
import os

from app import app
from embeddings_database.database import Database
from embeddings.extractor import EmbeddingExtractor
from scipy.spatial.distance import cosine


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
        print(f"Image {image_path} recognized as image {best_match[1]} with ID {best_match[0]} in the database.")
    else:
        print(f"Image {image_path} does not have a similar match in the database.")

def process_and_save_image(image_path):
    # Khởi tạo các đối tượng cần thiết
    extractor = EmbeddingExtractor()
    db = Database()

    # Lấy tên ảnh làm nhãn
    label = os.path.basename(os.path.dirname(image_path))
    # Lấy tên file từ đường dẫn (không bao gồm đường dẫn thư mục)

    # Kiểm tra xem ảnh đã có trong database chưa
    if db.check_image_exists(image_path):
        print(f"Image {image_path} already exists in the database.")
    else:
        # Trích xuất vector nhúng
        embedding = extractor.extract_embedding(image_path)
        if embedding is not None:
        # Lưu vào database với tên là nhãn
            db.save_embedding(image_path, label, embedding)
            print(f"[+]INFO: Image {image_path} has been processed and saved to the database with label {label}.")
        else:
            print(f"[!]WARNING: Could not process image {image_path}.")

    # Đóng kết nối database
    db.close()

if __name__ == "__main__":
    test_image_path = "./test_image"
    for root, dirs, files in os.walk(test_image_path):
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(root, filename)  # Thay đổi với đường dẫn ảnh thực tế
                process_and_save_image(image_path)

    image_path = r"demo/dm-tl-1.jpg"  # Thay đổi với đường dẫn ảnh thực tế
    recognize_image(image_path)

    # app.run(host='0.0.0.0', port=5000)
