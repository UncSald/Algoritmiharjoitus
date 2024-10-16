import unittest
from listMatrix import list_to_matrix, point_to_coord, rect_to_coord
from geometry import Rectangle

class TestListMatrix(unittest.TestCase):
    def test_rect_to_coord1(self):
        rect = Rectangle((0,0), 2, 2)
        result = rect_to_coord(rect, 1)
        expected = [(0,0),(1,0),
                    (0,1),(1,1)]
    def test_rect_to_coord2(self):
        rect = Rectangle((0,0), 5, 5)
        result = rect_to_coord(rect, 1)
        expected = [(0,0),(1,0),(2,0),(3,0),(4,0),
                    (0,1),(1,1),(2,1),(3,1),(4,1),
                    (0,2),(1,2),(2,2),(3,2),(4,2),
                    (0,3),(1,3),(2,3),(3,3),(4,3),
                    (0,4),(1,4),(2,4),(3,4),(4,4)]
        self.assertEqual(expected,result)
    def test_point_to_coord1(self):
        point = (0,0)
        result = point_to_coord(point,1)
        expected = (0,0)
        self.assertEqual(expected, result)
    
    def test_point_to_coord2(self):
        point = (64,128)
        result = point_to_coord(point,32)
        expected = (2,4)
        self.assertEqual(expected, result)

    def test_point_to_coord3(self):
        point = (63,127)
        result = point_to_coord(point,32)
        expected = (1,3)
        self.assertEqual(expected, result)

    def test_rect_list_to_matrix1(self):
        rect1 = Rectangle((1,1),3,3)
        rect_list = [rect1]
        rect_centers = [rect1.center]
        result = list_to_matrix(rect_list,rect_centers,5,5,(1,1),(2,2),1)
        expected = [
            [9,9,9,9,9],
            [9,3,1,1,9],
            [9,1,4,1,9],
            [9,1,1,1,9],
            [9,9,9,9,9]
        ]
        self.assertEqual(expected,result)

    def test_rect_list_to_matrix2(self):
        rect1 = Rectangle((1,1),2,2)
        rect2 = Rectangle((4,1),2,2)
        rect3 = Rectangle((1,4),3,3)
        rect_list = [rect1,rect2,rect3]
        rect_centers = [rect1.center,rect2.center,rect3.center]
        result = list_to_matrix(rect_list,rect_centers,10,10,(1,1),(2,5),1)
        expected = [
            [9,9,9,9,9,9,9,9,9,9],
            [9,3,1,0,1,1,0,0,0,9],
            [9,1,1,0,1,1,0,0,0,9],
            [9,0,0,0,0,0,0,0,0,9],
            [9,1,1,1,0,0,0,0,0,9],
            [9,1,4,1,0,0,0,0,0,9],
            [9,1,1,1,0,0,0,0,0,9],
            [9,0,0,0,0,0,0,0,0,9],
            [9,0,0,0,0,0,0,0,0,9],
            [9,9,9,9,9,9,9,9,9,9]
            ]
        self.assertEqual(expected,result)

if __name__ == "__main__":
    unittest.main()