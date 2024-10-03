import unittest
from geometry import Triangle

class TestTriangle(unittest.TestCase):

    def test_create_triangle1(self):
        triangle = Triangle((100,100), (101,101), (100,101))
        result = triangle._edges
        expected = [((100,100), (101,101)), ((100,100), (100,101)), ((101,101), (100,101))]
        self.assertEqual(expected, result)
    
    def test_triangle_circumcenter1(self):
        triangle = Triangle((100,100), (101,101), (100,101))
        result = triangle.circumcenter
        expected = (100.5, 100.5)
        self.assertEqual(expected, result)
    
    def test_triangle_circumcenter2(self):
        triangle = Triangle((500,120), (11,300), (123,432))
        x, y = triangle.circumcenter
        result = (round(x,3),round(y,3))
        expected = (254.395, 206.998)
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()