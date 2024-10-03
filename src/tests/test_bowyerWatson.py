import unittest
from random import randint
from bowyerWatson import BowyerWatson

class TestBowyerWatson(unittest.TestCase):

    def test_triangulation_size1(self):
        width, height = 500, 500
        expression = [(100,200), (300,400), (300,100)]
        BW = BowyerWatson(expression, width, height)
        BW.run()
        result = len(BW._triangulation)
        expected = 1
        self.assertEqual(result, expected)
    
    def test_triangulation_size2(self):
        width, height = 500, 500
        expression = [(100,200), (300,400), (300,100), (250,300), (100,400)]
        BW = BowyerWatson(expression, width, height)
        BW.run()
        result = len(BW._triangulation)
        expected = 4
        self.assertEqual(result, expected)

    def test_triangulation_size3(self):
        width, height = 500, 500
        expression = []
        for i in range(1000):
            point = (randint(0,499),randint(0,499))
            expression.append(point)
        BW = BowyerWatson(expression, width, height)
        BW.run()
        result = len(BW._triangulation)/100
        expected = 19.65
        self.assertAlmostEqual(result, expected, 0)


if __name__ == "__main__":
    unittest.main()
