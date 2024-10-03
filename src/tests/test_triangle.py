import unittest
from geometry import Triangle

class TestTriangle(unittest.TestCase):

    def test_create_triangle1(self):
        triangle = Triangle((100,100), (101,101), (100,101))
        result = triangle._edges
        expected = [((100,100), (101,101)), ((100,100), (100,101)), ((101,101), (100,101))]
        self.assertEqual(expected, result)
    

if __name__ == "__main__":
    unittest.main()