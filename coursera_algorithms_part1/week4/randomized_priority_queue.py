# Interview Questions: Priority Queues (ungraded)
# Practice Quiz, 3 questions
# Randomized priority queue. Describe how to add the
# methods 𝚜𝚊𝚖𝚙𝚕𝚎() and 𝚍𝚎𝚕𝚁𝚊𝚗𝚍𝚘𝚖() to our binary heap
# implementation. The two methods return a key that 
# is chosen uniformly at random among the remaining 
# keys, with the latter method also removing that key.
# The 𝚜𝚊𝚖𝚙𝚕𝚎() method should take constant time; the
# 𝚍𝚎𝚕𝚁𝚊𝚗𝚍𝚘𝚖() method should take logarithmic time.
# Do not worry about resizing the underlying array.


import unittest
import random


class RandomHeap:
    def __init__(self):
        self.arr = [0]
        self.size = 0

    def swim(self, idx):
        while idx != 1 and self.arr[idx//2] < self.arr[idx]:
            self.arr[idx], self.arr[idx//2] = self.arr[idx//2], self.arr[idx]
            idx = idx//2

    def sink(self, idx):
        while idx*2 <= self.size:
            mx_idx = idx*2
            if idx*2+1 <= self.size and self.arr[idx*2+1] > self.arr[idx*2]:
                mx_idx = idx*2+1
            if self.arr[mx_idx] > self.arr[idx]:
                self.arr[mx_idx], self.arr[idx] = self.arr[idx], self.arr[mx_idx]
                idx = mx_idx
            else:
                break

    def get_max(self):
        if self.size > 0:
            return self.arr[1]
        else:
            return None

    def del_max(self):
        if self.size > 0:
            mx = self.arr[1]
            self.arr[1] = self.arr[self.size]
            self.arr[self.size] = None
            self.size -= 1
            self.sink(1)
            return mx

    def insert(self, val):
        if len(self.arr)-1 <= self.size:
            self.arr.append(val)
        else:
            self.arr[self.size+1] = val
        self.size += 1
        self.swim(self.size)

    def empty(self):
        return self.size == 0

    def sample(self):
        if self.size > 0:
            return self.arr[random.randint(1, self.size)]

    def delRandom(self):
        if self.size > 0:
            idx = random.randint(1, self.size)
            val = self.arr[idx]
            self.arr[idx] = self.arr[self.size]
            self.arr[self.size] = None
            self.size -= 1
            mx_idx = None
            if idx*2 <= self.size and self.arr[idx*2] > self.arr[idx]:
                mx_idx = idx*2+1
            elif idx*2+1 <= self.size and self.arr[idx*2+1] > self.arr[2*idx]:
                mx_idx = idx*2+2
            if mx_idx:
                self.sink(idx)
            else:
                self.swim(idx)
            return val


class TestRandomHeap(unittest.TestCase):
    def setUp(self):
        size = 100
        self.arr = {random.randint(0, size*size) for x in range(size)}
        self.arr = [x for x in self.arr]

    def test_random_heap(self):
        random_heap = RandomHeap()
        self.assertEqual(random_heap.empty(), True)

        for each in self.arr:
            random_heap.insert(each)

        self.assertTrue(random_heap.sample() in self.arr)

        val = random_heap.delRandom()
        self.arr.remove(val)

        test = []
        while not random_heap.empty():
            test.append(random_heap.del_max())
        self.assertListEqual(sorted(self.arr, reverse=True), test)


if __name__ == '__main__':
    unittest.main()
