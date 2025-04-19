import os
from embeddings_database.database import Database
from embeddings.extractor import EmbeddingExtractor


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
            return True
        else:
            return False

    # Đóng kết nối database
    db.close()