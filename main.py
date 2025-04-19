# main.py
import os
from services.face_recognition import recognize_image
from services.face_save import process_and_save_image

if __name__ == "__main__":
    test_image_path = "./test_image"
    for root, dirs, files in os.walk(test_image_path):
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(root, filename)  # Thay đổi với đường dẫn ảnh thực tế
                if process_and_save_image(image_path):
                    print(f"[+]INFO: Processed and saved {image_path}")

    image_path = r"demo/dm-tl-2.jpg"  # Thay đổi với đường dẫn ảnh thực tế
    recognize_image(image_path)

    # app.run(host='0.0.0.0', port=5000)
