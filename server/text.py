import base64

def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64decode(img_file.read().decode('utf-8'))

get_base64_encoded_image('../dataset/Lional_messi/th (1).jpeg')
