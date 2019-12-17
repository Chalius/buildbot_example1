from archivo1 import Principal
import unittest

objeto = Principal;


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(objeto.suma(14, 12), 26, "Should be 26")


if __name__ == '__main__':
    unittest.main()
