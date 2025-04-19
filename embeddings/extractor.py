import cv2
from deepface import DeepFace

class EmbeddingExtractor:
    def __init__(self, model_name="VGG-Face"):
        self.model_name = model_name

    def detect_face(self, image_path):
        try:
        # Đọc ảnh từ đường dẫn
            img = cv2.imread(image_path)

            # Sử dụng OpenCV's Haar Cascade để phát hiện khuôn mặt
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            # Chuyển ảnh sang grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Phát hiện khuôn mặt trong ảnh
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            if len(faces) == 0:
                print("No face detected.")
                return None

            # Lấy khuôn mặt đầu tiên (nếu có nhiều hơn 1)
            x, y, w, h = faces[0]

            # Cắt ảnh chỉ giữ phần khuôn mặt
            face_img = img[y:y+h, x:x+w]
        except Exception as e:
            print("[!]ERROR: detecting face:", str(e))
            return None
        return face_img

    def resize_face(self, face_img, target_size=(224, 224)):
        # Thay đổi kích thước khuôn mặt về 224x224
        resized_face = cv2.resize(face_img, target_size)
        return resized_face

    def extract_embedding(self, image_path):
        # Phát hiện và cắt khuôn mặt
        face_img = self.detect_face(image_path)

        if face_img is None:
            return None

        # Thay đổi kích thước khuôn mặt về 224x224
        resized_face = self.resize_face(face_img)

        # Trích xuất embedding từ khuôn mặt đã thay đổi kích thước
        embedding = DeepFace.represent(resized_face, model_name=self.model_name, enforce_detection=False)

        return embedding[0]['embedding']