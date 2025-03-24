import sqlite3
import numpy as np
import json

class Database:
    def __init__(self, db_path='embeddings.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.conn.text_factory = str  # Đảm bảo dữ liệu được đọc đúng mã hóa (unicode)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Tạo bảng nếu chưa có
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS embeddings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT UNIQUE,
            label TEXT,
            embedding TEXT  -- Lưu embedding dưới dạng chuỗi JSON
        )
        ''')
        self.conn.commit()

    def save_embedding(self, image_path, label, embedding):
        # Chuyển vector thành chuỗi JSON
        embedding_json = json.dumps(embedding.tolist())  # Convert array to list and then to JSON string
        self.cursor.execute('''
        INSERT INTO embeddings (image_path, label, embedding) VALUES (?, ?, ?)
        ''', (image_path, label, embedding_json))
        self.conn.commit()

    def get_all_embeddings(self):
        # Lấy tất cả các vector nhúng từ database
        self.cursor.execute('SELECT image_path, label, embedding FROM embeddings')
        rows = self.cursor.fetchall()
        embeddings = []
        for row in rows:
            image_path = row[0]
            label = row[1]
            embedding_json = row[2]
            try:
                # Chuyển chuỗi JSON trở lại thành vector
                embedding = np.array(json.loads(embedding_json), dtype=np.float32)
                embeddings.append((image_path, label, embedding))
            except Exception as e:
                print(f"Error decoding embedding for {image_path}: {e}")
        return embeddings

    def check_image_exists(self, image_path):
        # Kiểm tra ảnh đã tồn tại trong database chưa
        self.cursor.execute('''
        SELECT id FROM embeddings WHERE image_path = ?
        ''', (image_path,))
        result = self.cursor.fetchone()
        return result is not None  # Nếu ảnh tồn tại, trả về True

    def close(self):
        self.conn.close()
