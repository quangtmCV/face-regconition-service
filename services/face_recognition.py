from embeddings.extractor import *
from embeddings_database.database import Database
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
        return best_match
    else:
        return None