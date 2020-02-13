# DAG: Design a linear-time algorithm to determine whether a 
# DAG has a vertex that is reachable from every other vertex, 
# and if so, find one

# Algorithm is to compute degree of each vertex 
# Exactly one vertex will have o out degree
# if there are more or less answer is no


import unittest
from digraph import DiGraph

class ReachableVertexDAG:
    def __init__(self, g):
        self.g = g
        self.reachable_vertex = self.traverse_graph()
    
    def traverse_graph(self):
        tmp = None
        for i in range(self.g.V):
            if len(self.g.adj(i)) == 0:
                if not tmp:
                    tmp = i
                else:
                    return None
        return tmp

    def get_reachable_vertex(self):
        return self.reachable_vertex


class TestReachableVertexDAG(unittest.TestCase):
    def test_exists(self):
        g = DiGraph(8)
        g.add_edge(0, 5)
        g.add_edge(0, 4)
        g.add_edge(6, 5)
        g.add_edge(7, 5)
        g.add_edge(3, 1)
        g.add_edge(2, 1)
        g.add_edge(1, 0)
        g.add_edge(4, 6)
        v = ReachableVertexDAG(g).get_reachable_vertex()
        self.assertEqual(v, 5)

    def test_does_not_exists(self):
        g = DiGraph(8)
        g.add_edge(0, 5)
        g.add_edge(0, 4)
        g.add_edge(6, 5)
        g.add_edge(7, 5)
        g.add_edge(3, 1)
        g.add_edge(1, 0)
        g.add_edge(4, 6)
        v = ReachableVertexDAG(g).get_reachable_vertex()
        self.assertEqual(v, None)

if __name__ == '__main__':
    unittest.main()
