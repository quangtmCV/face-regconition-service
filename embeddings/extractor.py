from deepface import DeepFace

class EmbeddingExtractor:
    def __init__(self, model_name="VGG-Face"):
        self.model_name = model_name

    def extract_embedding(self, image_path):
        # Trích xuất embedding từ ảnh
        embedding = DeepFace.represent(image_path, model_name=self.model_name, enforce_detection=False)
        return embedding[0]['embedding']
