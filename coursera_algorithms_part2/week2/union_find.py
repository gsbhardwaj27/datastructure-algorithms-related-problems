import unittest

class UnionFind:
    def __init__(self, size):
        self.weight = [1]*size
        self.parent = [x for x in range(size)]

    def union(self, x, y):
        xr = self.root(x)
        yr = self.root(y)
        if self.weight[xr] < self.weight[yr]:
            xr, yr = yr, xr
        self.parent[yr] = xr

    def root(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def find(self, x, y):
        return self.root(x) == self.root(y)

class testUnionFind(unittest.TestCase):
    def setUp(self):
        self.uf = UnionFind(8)

    def test_uf(self):
        self.uf.union(1, 2)
        self.uf.union(1, 3)
        self.uf.union(1, 4)
        self.uf.union(5, 6)
        self.uf.union(6, 7)
        self.assertEqual(self.uf.find(1, 2), True)
        self.assertEqual(self.uf.find(1, 6), False)
        self.assertEqual(self.uf.find(1, 4), True)


if __name__ == '__main__':
    unittest.main()
        

