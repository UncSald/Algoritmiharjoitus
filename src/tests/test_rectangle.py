import unittest
from geometry import Rectangle

class TestRectangle(unittest.TestCase):

    def test_rectangle_creation1(self):
        rect = Rectangle((100,100), 100, 100)
        result = (rect.up, rect.down, rect.left, rect.right)
        expected = (100, 200, 100, 200)
        self.assertEqual(expected, result)

    def test_rectangle_creation2(self):
        rect = Rectangle((567,420), 14, 210)
        result = (rect.up, rect.down, rect.left, rect.right)
        expected = (420, 630, 567, 581)
        self.assertEqual(expected, result)

    def test_rectangle_center1(self):
        pass

    def test_rectangle_center2(self):
        pass

    def test_rectangle_collisions1(self):
        pass

    def test_rectangle_collisions2(self):
        pass

    def test_rectangle_collisions3(self):
        pass

    def test_rectangle_collisions4(self):
        pass

if __name__ == "__main__":
    unittest.main()