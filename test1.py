from archivo1 import *
import unittest

objeto = Principal();


# print("mi suma: ", objeto.suma(5, 4))

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(objeto.suma(5, 4), 9)


if __name__ == '__main__':
    unittest.main()
