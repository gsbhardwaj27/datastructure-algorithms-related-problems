# Digraph: Design a linear-time algorithm to determine whether a 
# digraph has a vertex that is reachable from every other vertex, 
# and if so, find one.

import unittest
from digraph import DiGraph

class HamiltonPathDag:
    def __init__(self, g):
        self.g = g
        self.done = [False]*self.g.V
        self.topo_order = []
        self.populate_topo_order()
        self.has_hamilton_path = self._has_hamilton_path() 

    def populate_topo_order(self):
        for i in range(self.g.V):
            if not self.done[i]:
                self.topo_util(i)

    def get_reverse_topo_order(self):
        return list(reversed(self.topo_order))
                
    def topo_util(self, v):
        self.done[v] = True
        for each in self.g.adj(v):
            if not self.done[each]:
                self.topo_util(each)
        self.topo_order.append(v)

    def _has_hamilton_path(self):
        rto = self.get_reverse_topo_order()
        for i in range(len(rto)-1):
            if not (rto[i+1] in self.g.adj(rto[i])):
                return False
        return True
        

class TestHamiltonPathDag(unittest.TestCase):
    def test_topo_order(self):
        g = DiGraph(6)
        g.add_edge(2, 1)
        g.add_edge(1, 0)
        g.add_edge(0, 4)
        g.add_edge(4, 3)
        g.add_edge(3, 5)
        self.assertTrue(HamiltonPathDag(g).has_hamilton_path)        

    def test_topo_order(self):
        g = DiGraph(4)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 3)
        self.assertFalse(HamiltonPathDag(g).has_hamilton_path)        

    def test_topo_order(self):
        g = DiGraph(7)
        g.add_edge(2, 1)
        g.add_edge(1, 0)
        g.add_edge(0, 4)
        g.add_edge(4, 3)
        g.add_edge(3, 5)
        g.add_edge(6, 5)
        self.assertFalse(HamiltonPathDag(g).has_hamilton_path)        


if __name__ == '__main__':
    unittest.main()
