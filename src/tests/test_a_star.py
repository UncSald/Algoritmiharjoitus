import unittest
from a_star import a_star, weighted_graph

class TestAStar(unittest.TestCase):
    def test_weighted_graph1(self):
        matrix = [[9,9],
                  [9,9]]
        result = weighted_graph(matrix)
        expected = {
                    (0,0):[((0,1),6),((1,0),6)],
                    (0,1):[((0,0),6),((1,1),6)],
                    (1,0):[((0,0),6),((1,1),6)],
                    (1,1):[((0,1),6),((1,0),6)]
                    }
        self.assertEqual(expected,result)

    def test_weighted_graph2(self):
        matrix = [[9,0],
                  [1,2]]
        result = weighted_graph(matrix)
        expected = {
                    (0,0):[((0,1),2),((1,0),3)],
                    (0,1):[((0,0),5),((1,1),1)],
                    (1,0):[((0,0),5),((1,1),1)],
                    (1,1):[((0,1),2),((1,0),3)]
                    }
        self.assertEqual(expected,result)

    def test_a_star_path(self):
        graph = weighted_graph([[9,0],
                                [1,2]])
        result = a_star(graph,(0,0),(1,1))
        expected = {(0,0):None, (0,1):(0,0), (1,0):(0,0), (1,1):(0,1)}
        self.assertEqual(expected,result)


if __name__ == "__main__":
    unittest.main()