import os

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
IMAGE_DIR = os.path.join(ROOT_DIR, "Image_directory")

def make_sub_image_dir(image_names):
    try:
        sub_image_dir = get_sub_image_dir(image_names)
        if sub_image_dir:
            return make_dir(sub_image_dir)
    except Exception as e:
        return e

def make_dir(dir_name):
    try:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            return dir_name
    except Exception as e:
        return e

def get_sub_image_dir(image_name):
    if image_name:
        return os.path.join(IMAGE_DIR, image_name)
    else:
        return None

# def save_image_to_sub_dir(image):
#     try:
#         image_name = image.filename
#         sub_image_dir = make_sub_image_dir(image_name.split(".")[0])
#
#         # Define the full path to save the image
#         image_path = os.path.join(sub_image_dir, image_name)
#
#         # Save the image
#         image.save(image_path)
#
#         return image_path
#     except Exception as e:
#         return str(e)

