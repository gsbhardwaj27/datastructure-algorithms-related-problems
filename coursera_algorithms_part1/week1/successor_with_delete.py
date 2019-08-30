'''
Interview Questions: Union–Find (ungraded)

Successor with delete. Given a set of nn integers
S = { 0, 1, ... , n-1 }S={0,1,...,n−1} and
a sequence of requests of the following form:

Remove xx from SS
Find the successor of xx: the smallest yy in
SS such that y ge xy≥x.
'''


import unittest


class SuccessorWithDelete:
    def __init__(self, n):
        # As number of elements are fixed
        # We will create doubly linked list
        # array implementation
        self.conns = [[i-1, i+1] for i in range(n+1)]
        self.conns[-1][1] = 0

    def remove(self, x):
        if self.conns[x]:
            p, n = self.conns[x]
            self.conns[p][1] = n
            self.conns[n][0] = p
            self.conns[x] = None
            return True
        else:
            return False

    def successor(self, x):
        if self.conns[x]:
            return self.conns[x][1]
        else:
            return -1


class TestSuccessor(unittest.TestCase):
    def setUp(self):
        self.swd = SuccessorWithDelete(7)

    def test_uf(self):
        self.assertEqual(self.swd.successor(3), 4)
        self.swd.remove(4)
        self.assertEqual(self.swd.successor(3), 5)
        self.assertEqual(self.swd.successor(4), -1)


if __name__ == '__main__':
    unittest.main()
