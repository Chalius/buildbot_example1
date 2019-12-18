from archivo1 import Principal
import unittest

objeto = Principal;
print("mi suma: ", objeto.suma(5, 4))

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(objeto.suma(5, 4), 59)

if __name__ == '__main__':
    unittest.main()
