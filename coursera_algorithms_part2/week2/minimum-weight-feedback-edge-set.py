# Kruskal's Greedy implementation of MST
# Repeat belows steps untill mst does not have v-1 edges 
# or heap is not empty
# Find smallest edge, check if it does not create 
# a cycle in MST, if it does not add it to MSP else skip
# cycle shall be tested using Union Find data structure

import unittest

from union_find import UnionFind
from max_heap import MaxHeap
from edge_weighted_graph import Edge, EdgeWeightedGraph 


class MinWTFeedbackEdgeSet:
    def __init__(self, g):
        self.edge_set = []
        self.g = g
        self.heap = MaxHeap()
        self.UF = UnionFind(g.V)
        self.populateHeap()
        self.populate_edge_set()

    def populateHeap(self):
        edges = set()
        for i in range(self.g.V):
            for edge in self.g.adj(i):
                edges.add(edge)
        for edge in edges:
            self.heap.add_item(edge)

    def populate_edge_set(self):
        #import pdb; pdb.set_trace()
        while not self.heap.empty():
            edge = self.heap.del_max()
            if not self.UF.find(edge.either(), edge.other(edge.either())):
                self.UF.union(edge.either(), edge.other(edge.either()))
            else:
                self.edge_set.append(edge)
                    
    def get_mst(self):
        return self.edge_set


class TestMinWTFeedbackEdgeSet(unittest.TestCase):
    def test_mst(self):
        g = EdgeWeightedGraph(8)
        e01 = Edge(0, 1, 2) 
        g.add_edge(e01)
        e02 = Edge(0, 2, 10)
        g.add_edge(e02)
        e16 = Edge(1, 6, 19)
        g.add_edge(e16)
        e13 = Edge(1, 3, 25)
        g.add_edge(e13)
        e24 = Edge(2, 4, 10)
        g.add_edge(e24)
        e27 = Edge(2, 7, 5)
        g.add_edge(e27)
        e23 = Edge(2, 3, 16)
        g.add_edge(e23)
        e36 = Edge(3, 6, 6)
        g.add_edge(e36)
        e35 = Edge(3, 5, 4)
        g.add_edge(e35)
        e47 = Edge(4, 7, 9)
        g.add_edge(e47)
        e45 = Edge(4, 5, 11)
        g.add_edge(e45)
        print(MinWTFeedbackEdgeSet(g).get_mst())
        #self.assertListEqual(KruskalsMST(g).get_mst(), [e01, e35, e27, e36, e47, e02, e45])


if __name__ == '__main__':
    unittest.main()
