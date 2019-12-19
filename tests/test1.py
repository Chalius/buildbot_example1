# import archivo1
import unittest

import sys

sys.path.append("/home/chalius/connecttix/proyectsPycharm/pruebaTesting/ejem1")
from archivo1 import Principal




# print("mi suma: ", objeto.suma(5, 4))

class TestSum(unittest.TestCase):

    def test_sum(self):
        objeto = Principal();
        self.assertEqual(objeto.suma(5, 4), 9)


if __name__ == '__main__':
    unittest.main()
