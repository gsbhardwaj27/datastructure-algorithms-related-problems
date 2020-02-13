# DiGraph API

import unittest


class DiGraph:
    def __init__(self, v):
        self.V = v
        self.E = [[] for x in range(v)]

    def add_edge(self, v, w):
        self.E[v].append(w)

    def adj(self, v):
        return self.E[v]

    def degree(self, v):
        return len(self.E[v])

    def are_adj(self, v, w):
        for each in self.adj(v):
            if each==w:
                return True
        return False

    def add_vertex(self):
        self.V += 1
        self.E.append([]) 

    def populate_graph(self):
        edge_count = int(input())
        for i in range(edge_count()):
            v, w = map(int, (input().strip().split(' ')))
            self.add_edge(v, w)
    

class TestDiGraph(unittest.TestCase):
    def test_adj(self):
        g = DiGraph(10)
        g.add_edge(1, 2)
        g.add_edge(2, 4)
        g.add_edge(2, 6)
        g.add_edge(7, 8)
        g.add_edge(1, 8)

        self.assertTrue(g.are_adj(1, 8))
        self.assertFalse(g.are_adj(8, 1))
        self.assertFalse(g.are_adj(1, 9))

    def test_degree(self):
        g = DiGraph(10)
        g.add_edge(1, 2)
        g.add_edge(2, 4)
        g.add_edge(2, 6)
        g.add_edge(7, 8)
        g.add_edge(1, 8)

        self.assertTrue(g.degree(1)==2)
        self.assertTrue(g.degree(9)==0)
        self.assertTrue(g.degree(7)==1)

    def test_add_vertex(self):
        g = DiGraph(10)
        g.add_edge(1, 2)
        g.add_edge(2, 4)
        g.add_edge(2, 6)
        g.add_edge(7, 8)
        g.add_edge(1, 8)
        g.add_vertex()
        self.assertTrue(g.degree(10)==0)
        self.assertTrue(g.degree(1)==2)
        g.add_edge(10, 8)
        self.assertTrue(g.degree(10)==1)


if __name__ == '__main__':
    unittest.main()    
