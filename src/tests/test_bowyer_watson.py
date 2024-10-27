import unittest
from random import randint
from src.bowyer_watson import BowyerWatson

class TestBowyerWatson(unittest.TestCase):

    def test_triangulation_size1(self):
        width, height = 500, 500
        expression = [(100,200), (300,400), (300,100)]
        bw = BowyerWatson(expression, width, height)
        bw.run()
        result = len(bw.triangulation)
        expected = 1
        self.assertEqual(result, expected)
    
    def test_triangulation_size2(self):
        width, height = 500, 500
        expression = [(100,200), (300,400), (300,100), (250,300), (100,400)]
        bw = BowyerWatson(expression, width, height)
        bw.run()
        result = len(bw.triangulation)
        expected = 4
        self.assertEqual(result, expected)

    def test_triangulation_size3(self):
        width, height = 500, 500
        expression = []
        for i in range(1000):
            point = (randint(0,499),randint(0,499))
            expression.append(point)
        bw = BowyerWatson(expression, width, height)
        bw.run()
        result = len(bw.triangulation)/100
        expected = 19.65
        self.assertAlmostEqual(result, expected, 0)
    
    def test_error1(self):
        width, height = 500, 500
        expression = [(-1,3)]
        for i in range(100):
            point = (randint(0,499),randint(0,499))
            expression.append(point)
        bw = BowyerWatson(expression, width, height)
        bw.run()
        result = len(bw.points)
        expected = 100
        self.assertEqual(result, expected, 0)
    
    def test_error2(self):
        width, height = 500, -500
        expression = []
        for i in range(100):
            point = (randint(0,499),randint(0,499))
            expression.append(point)
        try:
            bw = BowyerWatson(expression, width, height)
            bw.run()
            assert False
        except ValueError:
            assert True

    def test_error3(self):
        width, height = 500, 500
        expression = []
        for i in range(2):
            point = (randint(0,499),randint(0,499))
            expression.append(point)
        try:
            bw = BowyerWatson(expression, width, height)
            bw.run()
            assert False
        except ValueError:
            assert True
    
    def test_error4(self):
        width, height = 500, 500
        expression = [(-1,3)]
        for i in range(2):
            point = (randint(0,499),randint(0,499))
            expression.append(point)
        try:
            bw = BowyerWatson(expression, width, height)
            bw.run()
            assert False
        except ValueError:
            assert True

if __name__ == "__main__":
    unittest.main()
