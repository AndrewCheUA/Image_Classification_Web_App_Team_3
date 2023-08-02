import numpy as np
from PIL import Image


def get_image_dimensions(image_path):
    """
    The get_image_dimensions function takes in a path to an image file and returns the width and height of that image.

    :param image_path: Specify the path to the image file
    :return: The width and height of an image
    """
    with Image.open(image_path) as img:
        width, height = img.size
        return width, height


def is_image(file_path):
    """
    The is_image function takes a file path as an argument and returns True if the file is an image, False otherwise.
    It uses the Pillow library to open the image and check that it can be opened without error.

    :param file_path: Specify the path of the file to be opened
    :return: True if the file is an image and false otherwise
    """
    try:
        with Image.open(file_path) as img:
            return True
    except:
        return False


def preprocess_image(image):
    """
    The preprocess_image function takes an image file path as input and returns a processed version of the image.
    The processing steps are:
        1. Open the image using PIL
        2. Convert the image to RGB mode (to ensure 3 color channels)
        3. Resize the image to 32x32 pixels (the size required by our model)
        4. Normalize the pixel values in each channel of the resized image to be between 0 and 1

    :param image: Pass the image to be preprocessed
    :return: A numpy array of shape (32, 32, 3)
    """
    test_image = Image.open(image).convert("RGB")  # Convert the image to RGB mode
    target_size = (32, 32)
    test_image = test_image.resize(target_size)

    image_array = np.array(test_image)

    image_array = image_array / 255.0

    input_image = np.expand_dims(image_array, axis=0)
    return input_image
