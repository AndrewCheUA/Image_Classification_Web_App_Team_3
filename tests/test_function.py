import unittest

from function.function import get_image_dimensions, is_image, preprocess_image


class TestImageUtils(unittest.TestCase):

    def test_get_image_dimensions(self):
        width, height = get_image_dimensions('test_image.jpg')
        self.assertEqual(width, 279)
        self.assertEqual(height, 181)

    def test_is_image_true(self):
        self.assertTrue(is_image('test_image.jpg'))

    def test_is_image_false(self):
        self.assertFalse(is_image('test.txt'))

    def test_preprocess_image(self):
        preprocessed = preprocess_image('test_image.jpg')
        self.assertEqual(preprocessed.shape, (1, 32, 32, 3))
        self.assertLessEqual(preprocessed.max(), 1.0)  # not normalized
        self.assertGreaterEqual(preprocessed.min(), -1.0)


if __name__ == '__main__':
    unittest.main()
