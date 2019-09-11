import unittest
import random


class DynamicMedian:
    def __init__(self):
        self.minH = MinHeap()
        self.maxH = MaxHeap()

    def insert(self, val):
        # breakpoint()
        if not self.maxH.size:
            self.maxH.insert(val)
        elif val <= self.maxH.get_max():
            if self.maxH.size > self.minH.size:
                self.minH.insert(self.maxH.del_max())
            self.maxH.insert(val)
        else:
            if not self.minH.size:
                self.minH.insert(val)
            elif self.minH.size > self.maxH.size:
                if val < self.minH.get_min():
                    self.maxH.insert(val)
                else:
                    self.maxH.insert(self.minH.del_min())
                    self.minH.insert(val)
            else:
                self.minH.insert(val)

    def del_median(self):
        if self.maxH.size > 0 or self.minH.size > 0:
            if self.maxH.size < self.minH.size:
                return self.minH.del_min()
            else:
                return self.maxH.del_max()

    def find_the_median(self):
        if self.minH.size > self.maxH.size:
            return self.minH.get_min()
        else:
            return self.maxH.get_max()


class MaxHeap:
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


class MinHeap:
    def __init__(self):
        self.arr = [0]
        self.size = 0

    def swim(self, idx):
        while idx != 1 and self.arr[idx//2] > self.arr[idx]:
            self.arr[idx], self.arr[idx//2] = self.arr[idx//2], self.arr[idx]
            idx = idx//2

    def sink(self, idx):
        while idx*2 <= self.size:
            mn_idx = idx*2
            if idx*2+1 <= self.size and self.arr[idx*2+1] < self.arr[idx*2]:
                mn_idx = idx*2+1
            if self.arr[mn_idx] < self.arr[idx]:
                self.arr[mn_idx], self.arr[idx] = self.arr[idx], self.arr[mn_idx]
                idx = mn_idx
            else:
                break

    def get_min(self):
        if self.size > 0:
            return self.arr[1]
        else:
            return None

    def del_min(self):
        if self.size > 0:
            mn = self.arr[1]
            self.arr[1] = self.arr[self.size]
            self.arr[self.size] = None
            self.size -= 1
            self.sink(1)
            return mn

    def insert(self, val):
        if len(self.arr)-1 <= self.size:
            self.arr.append(val)
        else:
            self.arr[self.size+1] = val
        self.size += 1
        self.swim(self.size)

    def empty(self):
        return self.size == 0


class TestDynamicMedian(unittest.TestCase):
    def setUp(self):
        self.dm = DynamicMedian()
        self.nums = []

    def test_dynamic_heap(self):
        mx = 1000
        num = random.randint(1, mx-1)
        self.nums.append(num)
        self.dm.insert(num)
        self.assertEqual(self.dm.find_the_median(), num)
        self.nums.append(num)
        self.dm.insert(num)
        self.assertEqual(self.dm.find_the_median(), num)
        for i in range(mx//10):
            num = random.randint(1, mx)
            self.nums.append(num)
            self.dm.insert(num)
            self.assertEqual(self.dm.find_the_median(), sorted(self.nums)[(len(self.nums)-1)//2])


if __name__ == '__main__':
    unittest.main()
