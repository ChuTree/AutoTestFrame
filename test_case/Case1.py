import unittest


class MyTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5,4+1)
    def test_Sub(self):
        self.assertEqual(4,5-1)


if __name__ == '__main__':
    unittest.main()

