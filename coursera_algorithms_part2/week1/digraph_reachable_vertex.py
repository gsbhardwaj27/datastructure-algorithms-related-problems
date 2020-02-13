# Digraph: Design a linear-time algorithm to determine whether a 
# digraph has a vertex that is reachable from every other vertex, 
# and if so, find one.

import unittest
from digraph import DiGraph

class DigraphHasReachableVertex:
    def __init__(self, g):
        self.g = g
        self.rg = None
        self.done = [False]*self.g.V
        self.topo_order = []
        self.cc_count = 0
        self.cc_id = [-1]*self.g.V       #Valid id are positive integeres starting from 1
        self.generate_reverse_graph()
        self.populate_topo_order()
        self.cc_dag = DiGraph(0)
        self.populate_strongly_cc_dag()

    def populate_topo_order(self):
        for i in range(self.rg.V):
            if not self.done[i]:
                self.topo_util(i, self.rg)

    def get_reverse_topo_order(self):
        return list(reversed(self.topo_order))
                
    def topo_util(self, v, g):
        self.done[v] = True
        for each in g.adj(v):
            if not self.done[each]:
                self.topo_util(each, g)
        self.topo_order.append(v)
        
    def generate_reverse_graph(self):
        self.rg = DiGraph(self.g.V)
        for i in range(self.rg.V):
            for j in self.g.adj(i):
                self.rg.add_edge(j, i)
    
    def populate_strongly_cc_dag(self):
        self.done = [False]*self.g.V
        for each in self.get_reverse_topo_order():
            if not self.done[each]:
                self.cc_count += 1
                self.cc_dag.add_vertex()
                self.cc_dfs(each)

    def cc_dfs(self, v):
        self.done[v] = True
        self.cc_id[v] = self.cc_count-1
        for each in self.g.adj(v):
            if self.done[each] and self.cc_id[each] != self.cc_id[v]:
                self.cc_dag.add_edge(self.cc_count-1, self.cc_id[each])
            if not self.done[each]:
                self.cc_dfs(each) 

    def has_rechable_vertex(self):
        zero_degree_count = 0
        for i in range(self.cc_dag.V):
            if len(self.cc_dag.adj(i))==0:
                zero_degree_count += 1
                if zero_degree_count > 1:
                    return False
        if zero_degree_count == 0:
            return False
        return True
             


class TestDigraphHasReachableVertex(unittest.TestCase):
    def test_topo_order(self):
        g = DiGraph(6)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 0)
        g.add_edge(2, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 4)
        rto = DigraphHasReachableVertex(g).get_reverse_topo_order()
        self.assertListEqual(rto, [4, 5, 1, 0, 3, 2])        

    def test_component_count(self):
        g = DiGraph(6)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 0)
        g.add_edge(2, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 4)
        self.assertFalse(DigraphHasReachableVertex(g).has_rechable_vertex())        

    def test_strongly_connected(self):
        g = DiGraph(6)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        g.add_edge(2, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 3)
        g.add_edge(5, 3)
        self.assertTrue(DigraphHasReachableVertex(g).has_rechable_vertex())


if __name__ == '__main__':
    unittest.main()
