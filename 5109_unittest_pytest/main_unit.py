import unittest
from reverse import reverse

class TestReverse(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(reverse(''), '')

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            reverse(42)

    def test_single_char(self):
        self.assertEqual(reverse('f'), 'f')


if __name__ == '__main__':
    unittest.main()