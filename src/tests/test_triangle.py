import unittest
from geometry import Triangle

class TestTriangle(unittest.TestCase):

    def test_create_triangle1(self):
        triangle = Triangle((100,100), (101,101), (100,101))
        result = triangle._edges
        expected = [((100,100), (101,101)), ((100,100), (100,101)), ((101,101), (100,101))]
        self.assertEqual(expected, result)
    
    # CIRCUMCENTERS CHECKED AT https://byjus.com/circumcenter-calculator/
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

    # EDGE LENGHTS CHECKED AT https://www.calculatorsoup.com/calculators/geometry-plane/distance-two-points.php
    def test_triangle_edges_len1(self):
        triangle = Triangle((100,100), (101,101), (100,101))
        result_a = round(triangle.a_edge_len, 5)
        result_b = round(triangle.b_edge_len, 5)
        result_c = round(triangle.c_edge_len, 5)
        expected_a = 1.41421
        expected_b = 1
        expected_c = 1
        self.assertEqual(expected_a, result_a)
        self.assertEqual(expected_b, result_b)
        self.assertEqual(expected_c, result_c)

    def test_triangle_edge_len2(self):
        triangle = Triangle((500,120), (11,300), (123,432))
        result_a = round(triangle.a_edge_len, 5)
        result_b = round(triangle.b_edge_len, 5)
        result_c = round(triangle.c_edge_len, 5)
        expected_a = 521.07677
        expected_b = 489.35979
        expected_c = 173.11268
        self.assertEqual(expected_a, result_a)
        self.assertEqual(expected_b, result_b)
        self.assertEqual(expected_c, result_c)

    # TRIANGLE ANGLES CHECKED AT https://www.calculator.net/triangle-calculator.html
    def test_triangle_angles1(self):
        triangle = Triangle((100,100), (101,101), (100,101))
        result_a = round(triangle.a_angle,4)
        result_b = round(triangle.b_angle,4)
        result_c = round(triangle.c_angle,4)
        expected_a = 0.7854
        expected_b = 0.7854
        expected_c = 1.5708
        self.assertEqual(expected_a, result_a)
        self.assertEqual(expected_b, result_b)
        self.assertEqual(expected_c, result_c)

    def test_triangle_angles1(self):
        triangle = Triangle((500,120), (11,300), (123,432))
        result_a = round(triangle.a_angle,4)
        result_b = round(triangle.b_angle,4)
        result_c = round(triangle.c_angle,4)
        expected_a = 0.3386
        expected_b = 1.2199
        expected_c = 1.5831
        self.assertEqual(expected_a, result_a)
        self.assertEqual(expected_b, result_b)
        self.assertEqual(expected_c, result_c)

if __name__ == "__main__":
    unittest.main()