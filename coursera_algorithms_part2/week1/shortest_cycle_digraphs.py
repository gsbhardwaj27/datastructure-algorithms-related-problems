# Find shortest cycle length in a directed 
# cyclic graph 
# Shortest directed cycle. Given a digraph GG, design an efficient 
# algorithm to find a directed cycle with the minimum number of 
# edges (or report that the graph is acyclic). The running time 
# of your algorithm should be at most proportional to 
# V(E + V)V(E+V) and use space proportional to E + VE+V, 
# where VV is the number of vertices and EE is the number of edges.

import unittest
from digraph import DiGraph

class SmallestCycle:
    def __init__(self, g):
        self.g = g
        self.rg = None
        self.done = [False]*self.g.V
        self.done_ = [False]*self.g.V # Maintain for current run
        self.pos = [-1]*self.g.V
        self.min_cycle_len = self.g.V + 2 # setting a high value
        self.traverse_graph()
    
    def traverse_graph(self):
        for i in range(self.g.V):
            if not self.done[i]:
                self.pos = [-1]*self.g.V
                self.done_ = [False]*self.g.V
                self.dfs(i, 0)

    def dfs(self, v, curr_pos):
        self.done[v] = self.done_[v] = True
        self.pos[v] = curr_pos
        for each in self.g.adj(v):
            if not self.done_[each]:
                self.dfs(each, curr_pos+1)
            elif curr_pos - self.pos[each] + 1 < self.min_cycle_len:
                self.min_cycle_len = curr_pos - self.pos[each] + 1
    
    def get_smallest_cycle_length(self):
        if self.min_cycle_len == self.g.V + 2:
            return None
        else:
            return self.min_cycle_len


class TestSmallestCycle(unittest.TestCase):
    def test_length1(self):
        g = DiGraph(7)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(3, 4)
        g.add_edge(3, 6)
        g.add_edge(6, 3)
        g.add_edge(4, 5)
        g.add_edge(5, 3)
        g.add_edge(5, 0)
        l = SmallestCycle(g).get_smallest_cycle_length()
        self.assertEqual(l, 2)

    def test_length2(self):
        g = DiGraph(7)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 3)
        g.add_edge(5, 0)
        l = SmallestCycle(g).get_smallest_cycle_length()
        self.assertEqual(l, 3)

    def test_no_cycle(self):
        g = DiGraph(7)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(3, 4)
        g.add_edge(4, 5)
        l = SmallestCycle(g).get_smallest_cycle_length()
        self.assertEqual(l, None)

if __name__ == '__main__':
    unittest.main()
