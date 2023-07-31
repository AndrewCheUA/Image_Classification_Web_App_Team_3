from PIL import Image


def get_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        return width, height


def is_image(file_path):
    try:
        with Image.open(file_path) as img:
            return True
    except:
        return False