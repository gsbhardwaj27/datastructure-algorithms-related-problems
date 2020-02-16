import unittest


class Edge:
    def __init__(self, v, w, wt):
        self.v = v
        self.w = w
        self.wt = wt

    def __eq__(self, edge):
        return self.wt == edge.wt

    def __lt__(self, edge):
        return self.wt < edge.wt

    def __gt__(self, edge):
        return self.wt > edge.wt

    def either(self):
        return self.v

    def other(self, vertex):
        if self.v==vertex:
            return self.w
        else:
            return self.v
    
    def __repr__(self):
        return f'--{self.v}, {self.w}, {self.wt}--'


class EdgeWeightedGraph:
    def __init__(self, v):
        self.V = v
        self.edges = [[] for x in range(self.V)]

    def adj(self, v):
        return self.edges[v]

    def add_edge(self, edge):
        self.edges[edge.either()].append(edge)
        self.edges[edge.other(edge.either())].append(edge)


class TestEdge(unittest.TestCase):
    def test_either(self):
        e = Edge(1, 2, 10)
        self.assertEqual(e.either(), 1)

    def test_other(self):
        e = Edge(1, 2, 10)
        self.assertEqual(e.other(1), 2)

    def test_comp(self):
        e1 = Edge(1, 2, 10)
        e2 = Edge(4, 5, 11)
        self.assertTrue(e1 < e2)
        self.assertFalse(e2 < e1)
        self.assertTrue(e1 == e1)
        

if __name__ == '__main__':
    unittest.main()
