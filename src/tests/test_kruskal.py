import unittest
from kruskal import kruskal

class test_kruskal(unittest.TestCase):

    # TESTS CHECK IF THE KRUSKAL ALGORITHM RETURNS THE CORRECT AMOUNT OF
    # EDGES AFTER EING GIVEN A LIST OF EDGES
    # THERE SHOULD ALWAYS BE 1 LESS EDGES THAN THERE ARE POINTS IN A
    # MINIMUM SPANNING TREE
    def test_edge_count1(self):
        input = (((100,100),(200,200)),
        ((200,200),(150,200)),
        ((150,200),(200,100)),
        ((100,100),(200,100)))
        result = len(kruskal(input, (100,100)))
        expected = 3
        self.assertEqual(expected,result)

    def test_edge_count2(self):
        input = set()
        points = [(i,i) for i in range(10)]
        for i in points:
            for j in points:
                input.add((i,j))
        result = len(kruskal(input,(1,1)))
        expected = len(points)-1
        self.assertEqual(expected, result)

    def test_edge_count3(self):
        input = set()
        points = [(i,i) for i in range(1000)]
        for i in points:
            for j in points:
                input.add((i,j))
        result = len(kruskal(input,(1,1)))
        expected = len(points)-1
        self.assertEqual(expected, result)
    
    
    
    
    # TESTS TO CHECK IF ALL POINTS ARE INCLUDED IN THE MST
    def test_all_points_in_mst1(self):
        input = set()
        points = [(i,i) for i in range(10)]
        result = True
        for i in points:
            for j in points:
                input.add((i,j))
        for point in points:
            result = False
            for edge in input:
                if point in edge:
                    result = True
            if result is False:
                break
        expected = True
        self.assertEqual(expected, result)
    
    def test_all_points_in_mst2(self):
        input = set()
        points = [(i,i) for i in range(100)]
        result = True
        for i in points:
            for j in points:
                input.add((i,j))
        for point in points:
            result = False
            for edge in input:
                if point in edge:
                    result = True
            if result is False:
                break
        expected = True
        self.assertEqual(expected, result)




if __name__ == "__main__":
    unittest.main()