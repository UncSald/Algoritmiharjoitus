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
        pass
    def test_rect_list_to_matrix1(self):
        pass

if __name__ == "__main__":
    unittest.main()