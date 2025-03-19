# from deepface import DeepFace
#
# def recognize_character(image_path):
#     try:
#         # Perform face recognition
#         result = DeepFace.find(img_path=image_path, db_path="path/to/your/database", enforce_detection=False)
#
#         # Check if any faces were found
#         if len(result) > 0:
#             # Return the name of the character
#             return result[0]['identity']
#         else:
#             return "No character recognized"
#     except Exception as e:
#         return f"Error: {e}"
#
# # Example usage
# if __name__ == "__main__":
#     test_image_path = r"E:\quangtm\AS_IT\Projects\AS_product_project\face-regconition-service\test_image\shawn_mendes_6.jpg"
#     character_name = recognize_character(test_image_path)
#     print(f"Character recognized: {character_name}")

from deepface import DeepFace

def recognize_character(image_path, known_image_path):
    try:
        # Perform face verification
        result = DeepFace.verify(img1_path=image_path, img2_path=known_image_path, enforce_detection=False)

        # Check if the faces match
        if result["verified"]:
            return "Character recognized"
        else:
            return "No character recognized"
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    test_image_path = r"/test_image/shawn_mendes_6.jpg"
    known_image_path = r"E:\quangtm\AS_IT\Projects\AS_product_project\face-regconition-service\known_images\shawn_mendes_1.jpg"
    character_name = recognize_character(test_image_path, known_image_path)
    print(f"Character recognized: {character_name}")