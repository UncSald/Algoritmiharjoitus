import unittest
from geometry import Triangle

class TestTriangle(unittest.TestCase):

    def test_create_triangle1(self):
        triangle = Triangle((100,100), (101,101), (100,101))
        result = triangle.edges
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

    # RADIUS CHECKED AT https://www.omnicalculator.com/math/circumscribed-circle
    def test_circumcircle_radius1(self):
        triangle = Triangle((100,100), (101,101), (100,101))
        result = round(triangle.radius,4)
        expected = 0.7071
        self.assertEqual(expected, result)

    def test_circumcircle_radius2(self):
        triangle = Triangle((500,120), (11,300), (123,432))
        result = round(triangle.radius,2)
        expected = 260.56
        self.assertEqual(expected, result)


    def test_check_point1(self):
        triangle = Triangle((100,100), (101,101), (100,101))
        point = (100.5,100)
        result = triangle.check_point(point)
        expected = True
        self.assertEqual(expected, result)

    def test_check_point2(self):
        triangle = Triangle((100,100), (101,101), (100,101))
        point = (200.5,100)
        result = triangle.check_point(point)
        expected = False
        self.assertEqual(expected, result)

    def test_check_point3(self):
        triangle = Triangle((500,120), (11,300), (123,432))
        point = (100.5,300)
        result = triangle.check_point(point)
        expected = True
        self.assertEqual(expected, result)

    def test_check_point4(self):
        triangle = Triangle((500,120), (11,300), (123,432))
        point = (500.0001,119.9999)
        result = triangle.check_point(point)
        expected = False
        self.assertEqual(expected, result)
    


if __name__ == "__main__":
    unittest.main()