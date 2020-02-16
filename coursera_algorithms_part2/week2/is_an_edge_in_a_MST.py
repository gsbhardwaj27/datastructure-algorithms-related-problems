# Is an edge in a MST. Given an edge-weighted graph GG and an edge ee, 
# design a linear-time algorithm to determine whether ee appears in some MST of GG.
# Check if its smallest edge of the node
# Yes than it will always be in MST
# No than check if this edge is a bridge
# yes then it will be in MST else
# may not be part of ant MST


import unittest

from edge_weighted_graph import Edge, EdgeWeightedGraph 


class IsAnEdgeInAMST:
    def __init__(self, g):
        self.g = g
        self.done = [False]*self.g.V
    
    def is_edge_in_mst(self, edge):
        if self._is_min_weight_edge(edge):
            return True
        elif self._is_bridge(edge):
            return True
        return False
        
    def _is_bridge(self, edge):
        self.done = [False]*self.g.V
        self._dfs(edge.either(), edge)
        if False in self.done:
            return True
        else:
            return False
        
    def _dfs(self, node, skip_edge):
        self.done[node] = True
        for each in self.g.adj(node):
            if not each is skip_edge and \
                not self.done[each.other(node)]:
                self._dfs(each.other(node), skip_edge)

    def _is_min_weight_edge(self, edge):
        either = edge.either()
        other = edge.other(edge.either())
        min_wt_either = min(self.g.adj(either), key=lambda x: x.wt).wt
        if min_wt_either == edge.wt:
            return True
        min_wt_other = min(self.g.adj(other), key=lambda x: x.wt).wt
        if min_wt_other == edge.wt:
            return True
        return False
             

class TestIsAnEdgeInAMST(unittest.TestCase):
    def test_edge_in_mst(self):
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
        self.assertTrue(IsAnEdgeInAMST(g).is_edge_in_mst(e01))
        self.assertFalse(IsAnEdgeInAMST(g).is_edge_in_mst(e13))
        self.assertFalse(IsAnEdgeInAMST(g).is_edge_in_mst(e23))
        self.assertTrue(IsAnEdgeInAMST(g).is_edge_in_mst(e27))



if __name__ == '__main__':
    unittest.main()
