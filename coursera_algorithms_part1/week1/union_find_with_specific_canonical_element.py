'''
Interview Questions: Union–Find (ungraded)

Union-find with specific canonical element.

Add a method 𝚏𝚒𝚗𝚍() to the union-find data
type so that 𝚏𝚒𝚗𝚍(𝚒) returns the largest
element in the connected component containing ii.
The operations, 𝚞𝚗𝚒𝚘𝚗(), 𝚌𝚘𝚗𝚗𝚎𝚌𝚝𝚎𝚍(), and 𝚏𝚒𝚗𝚍()
should all take logarithmic time or better.

For example, if one of the connected components 
is {1, 2, 6, 9}{1,2,6,9}, then the 𝚏𝚒𝚗𝚍() method
should return 99 for each of the four elements in
the connected components.
'''


import unittest


class UnionFindWithSpecificCanonicalElement:
    def __init__(self, n):
        self.conns = [i for i in range(n+1)]
        self.weights = [1]*(n+1)

    def union(self, x, y):
        first = self.root(x)
        second = self.root(y)
        # Idea here is we will make sure
        # root is always bigger then nodes
        # attached to it
        # we will have disadvantages due to it 
        # that instead of Mlog*N our complexity
        # will be MlogN for N elements and M ops
        if first > second:
            first, second = second, first
        self.conns[first] = self.conns[second]
        self.weights[second] += self.weights[first]

    def root(self, x):
        i = x
        # Path compression will make sure
        # log(n) complexity
        while i != self.conns[i]:
            self.conns[i] = self.conns[self.conns[i]]
            i = self.conns[i]
        return i

    def find(self, x):
        return self.root(x)


class TestConnectivity(unittest.TestCase):
    def setUp(self):
        self.uf = UnionFindWithSpecificCanonicalElement(7)
    
    def test_uf(self):
        self.uf.union(1, 2)
        self.uf.union(1, 3)
        self.uf.union(1, 4)
        self.uf.union(5, 6)
        self.uf.union(6, 7)
        self.assertEqual(self.uf.find(1), 4)
        self.assertEqual(self.uf.find(2), 4)
        self.assertEqual(self.uf.find(5), 7)
        self.uf.union(1, 5)
        self.assertEqual(self.uf.find(2), 7)


if __name__ == '__main__':
    unittest.main()
