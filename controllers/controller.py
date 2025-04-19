# controllers/controller.py
import os
import uuid
from flask import request, jsonify
from werkzeug.utils import secure_filename

class Controller:
    def __init__(self):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'faces'))
        os.makedirs(self.base_dir, exist_ok=True)

    def register_face(self):
        try:
            # Get the uploaded file and user name
            image = request.files.get('image')
            name = request.form.get('name')

            if not image or not name:
                return jsonify({'error': 'Name and image are required'}), 400

            # Secure the file name and create a user directory
            user_dir = os.path.join(self.base_dir, secure_filename(name))
            os.makedirs(user_dir, exist_ok=True)

            # Save the image with a unique name
            image_path = os.path.join(user_dir, f'{uuid.uuid4()}.jpg')
            image.save(image_path)

            return jsonify({'message': 'Face registered successfully', 'path': image_path}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500