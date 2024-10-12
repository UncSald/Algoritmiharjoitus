import unittest
from a_star import a_star, weighted_graph

class TestAStar(unittest.TestCase):
    def test_weighted_graph1(self):
        matrix = [[9,9],
                  [9,9]]
        result = weighted_graph(matrix)
        expected = {
                    (0,0):[((0,1),4),((1,0),4)],
                    (0,1):[((0,0),4),((1,1),4)],
                    (1,0):[((0,0),4),((1,1),4)],
                    (1,1):[((0,1),4),((1,0),4)]
                    }
        self.assertEqual(expected,result)

if __name__ == "__main__":
    unittest.main()