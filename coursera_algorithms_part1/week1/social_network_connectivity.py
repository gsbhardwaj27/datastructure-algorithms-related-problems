'''
Interview Questions: Union–Find (ungraded)
Practice Quiz, 3 questions
Social network connectivity.

Given a social network containing nn members and a log
file containing mm timestamps at which times pairs of
members formed friendships, design an algorithm to
determine the earliest time at which all members
are connected (i.e., every member is a friend of a
friend of a friend ... of a friend). Assume that the
log file is sorted by timestamp and that friendship is
an equivalence relation. The running time of your
algorithm should be m log nmlogn or better and
use extra space proportional to nn.
'''


import unittest


class SocialNetworkConnectivity:
    def __init__(self, n):
        self.conns = [i for i in range(n+1)]
        self.weights = [1]*(n+1)

    def connect(self, x, y):
        first = self.root(x)
        second = self.root(y)

        if self.weights[first] > self.weights[second]:
            first, second = second, first
        self.conns[first] = self.conns[second]
        self.weights[second] += self.weights[first]

    def root(self, x):
        i = x
        while i != self.conns[i]:
            self.conns[i] = self.conns[self.conns[i]]
            i = self.conns[i]
        return i

    def has_all(self, x):
        return self.weights[self.root(x)] == (len(self.conns)-1)


class TestConnectivity(unittest.TestCase):
    def setUp(self):
        self.sn = SocialNetworkConnectivity(7)

    def test_basic(self):
        # input file
        # Timestamp userid1 userid2
        # 123 1 2
        # 124 1 4
        # 125 1 3
        # 139 5 6
        # 140 6 7
        # 142 4 7
        # 187 1 7

        # All users are connected at time stamp 142
        all_connected_time = None
        with open('social_network_connectivity.txt') as f:
            for line in f:
                timestamp, user1, user2 = tuple(map(int, line.split()))
                self.sn.connect(user1, user2)
                if self.sn.has_all(user1) or self.sn.has_all(user2):
                    all_connected_time = timestamp
                    break
        self.assertEqual(142, all_connected_time)


if __name__ == '__main__':
    unittest.main()
