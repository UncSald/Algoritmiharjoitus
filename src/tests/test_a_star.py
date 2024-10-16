import unittest
from a_star import a_star, weighted_graph, shortest_path, build_path

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

    def test_a_star_path1(self):
        graph = weighted_graph([[9,0],
                                [1,2]])
        result = a_star(graph,(0,0),(1,1))
        expected = {(0,0):None,
                    (0,1):(0,0),
                    (1,0):(0,0),
                    (1,1):(0,1)}
        self.assertEqual(expected,result)

    def test_a_star_path2(self):
        graph = weighted_graph([[9,0,4],
                                [9,0,2],
                                [1,3,2]])
        result = a_star(graph,(2,1),(0,2))
        expected = {(2,1):None,
                    (2,0):(2,1),
                    (1,1):(2,1),
                    (2,2):(2,1),
                    (1,2):(2,2),
                    (0,2):(1,2)}
        self.assertEqual(expected,result)

    def test_shortest_path1(self):
        graph = weighted_graph([[9,0],
                                [1,2]])
        result = shortest_path(a_star(graph,(0,0),(1,1)),(0,0),(1,1))
        expected = [(1,1),(0,1),(0,0)]
        self.assertEqual(expected,result)

    def test_shortest_path2(self):
        graph = weighted_graph([[9,2,4,0,0],
                                [9,2,0,0,0],
                                [9,2,2,2,2],
                                [9,9,9,9,2],
                                [1,3,2,2,2]])
        result = shortest_path(a_star(graph,(4,1),(0,2)),(4,1),(0,2))
        expected = [(0,2),(0,1),(1,1),(2,1),(3,1),(4,1)]
        self.assertEqual(expected,result)
    
    def test_build_path1(self):
        matrix = [
            [9,2,4,0,0],
            [9,2,0,0,0],
            [9,2,2,2,2],
            [9,9,9,9,2],
            [1,3,2,2,2]
            ]
        result = build_path(matrix, [((1,4),(2,0))], 1)
        expected = [
            [9,2,4,0,0],
            [9,2,0,0,0],
            [9,2,2,2,2],
            [9,2,9,9,2],
            [1,3,2,2,2]
            ]
        self.assertEqual(expected,result)
    def test_build_path2(self):
        matrix = [[9,9,4,1,0],
                  [9,9,0,0,0],
                  [9,9,9,9,2],
                  [9,9,9,9,2],
                  [1,3,2,2,2]]
        result = build_path(matrix, [((1,4),(2,0))], 1)
        expected = [
            [9,9,4,1,0],
            [9,9,2,2,2],
            [9,9,9,9,2],
            [9,9,9,9,2],
            [1,3,2,2,2]
            ]
        self.assertEqual(expected,result)

    def test_build_path3(self):
        matrix = [
            [9,0,4,1,9,2],
            [9,0,9,1,9,2],
            [9,0,9,1,9,2],
            [9,0,9,1,9,2],
            [9,0,9,1,9,2],
            [9,0,3,0,2,2]]
        result = build_path(matrix, [((1,5),(2,0))], 1)
        expected = [
            [9,2,4,1,9,2],
            [9,2,9,1,9,2],
            [9,2,9,1,9,2],
            [9,2,9,1,9,2],
            [9,2,9,1,9,2],
            [9,2,3,0,2,2]]
        self.assertEqual(expected,result)
if __name__ == "__main__":
    unittest.main()