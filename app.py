from flask import Flask, request, jsonify
import helper.dir
import services.face_services

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def register_image():
    try:
        # Get the uploaded file
        image = request.files.get('image')
        if not image:
            return jsonify({'error': 'No image uploaded'}), 400
        else:
            image_name = image.filename
            # Create sub image directory
            sub_image_dir = helper.dir.make_sub_image_dir(image_name.split(".")[0])
            # Save the image to sub image directory
            face_service = services.face_services.FaceService()
            image_path = face_service.save_image_to_sub_dir(image=image, sub_image_dir=sub_image_dir)

            return jsonify({'message': 'Image received successfully. Added to database.', 'filename': image_name, 'image_path': image_path},), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

register_image()

# @app.route('/api/recognize', methods=['POST'])
