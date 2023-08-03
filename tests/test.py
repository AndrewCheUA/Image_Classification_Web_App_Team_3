import os
import unittest

from function.function import get_image_dimensions, is_image, preprocess_image

print("Current directory:", os.getcwd())

class TestImageUtils(unittest.TestCase):

    def test_get_image_dimensions(self):
        image_path = os.path.join(os.path.dirname(__file__), "test_image.jpg")
        width, height = get_image_dimensions(image_path)
        self.assertEqual(width, 279)
        self.assertEqual(height, 181)

    def test_is_image_true(self):
        image_path = os.path.join(os.path.dirname(__file__), "test_image.jpg")
        self.assertTrue(is_image(image_path))

    def test_is_image_false(self):
        self.assertFalse(is_image('test.txt'))

    def test_preprocess_image(self):
        image_path = os.path.join(os.path.dirname(__file__), "test_image.jpg")
        preprocessed = preprocess_image(image_path)
        self.assertEqual(preprocessed.shape, (1, 32, 32, 3))
        self.assertLessEqual(preprocessed.max(), 1.0)  # not normalized
        self.assertGreaterEqual(preprocessed.min(), -1.0)


if __name__ == '__main__':
    unittest.main()
