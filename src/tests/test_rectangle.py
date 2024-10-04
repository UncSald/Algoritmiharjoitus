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
        rect = Rectangle((100,100), 100, 100)
        result = rect.center
        expected = (150,150)
        self.assertEqual(expected, result)

    def test_rectangle_center2(self):
        rect = Rectangle((567,420), 14, 210)
        result = rect.center
        expected = (574,525)
        self.assertEqual(expected, result)

    def test_rectangle_collisions1(self):
        rect1 = Rectangle((100,100), 100, 100)
        rect2 = Rectangle((201,201), 14, 210)
        result = rect1.collision(rect2)
        expected = False
        self.assertEqual(expected,result)

    def test_rectangle_collisions2(self):
        rect1 = Rectangle((100,100), 100, 100)
        rect2 = Rectangle((200,200), 100, 100)
        result = rect1.collision(rect2)
        expected = True
        self.assertEqual(expected, result)

    def test_rectangle_collisions3(self):
        rect1 = Rectangle((100,100), 100, 100)
        rect2 = Rectangle((120,120), 10, 10)
        result = rect1.collision(rect2)
        expected = True
        self.assertEqual(expected, result)

    def test_rectangle_collisions4(self):
        rect1 = Rectangle((100,100), 100, 100)
        rect2 = Rectangle((90,110), 120, 80)
        result = rect1.collision(rect2)
        expected = True
        self.assertEqual(expected, result)
    
    def test_rectangle_collisions4(self):
        rect1 = Rectangle((100,100), 100, 100)
        rect2 = Rectangle((110,90), 80, 120)
        result = rect1.collision(rect2)
        expected = True
        self.assertEqual(expected, result)

if __name__ == "__main__":
    unittest.main()