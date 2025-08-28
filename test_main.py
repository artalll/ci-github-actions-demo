import unittest
from main import add

class TestAdd(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add(2,3),5)

if __name__=="main":
    unittest.main()
