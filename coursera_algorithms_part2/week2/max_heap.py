import unittest
import random


class MaxHeap:
    def __init__(self):
        self.size = 0
        self.arr = []


    def swim(self, idx):
        while idx > 0:
            if self.arr[(idx-1)//2] < self.arr[idx]:
                self.arr[(idx-1)//2], self.arr[idx] = self.arr[idx], self.arr[(idx-1)//2]
                idx = (idx-1)//2
            else:
                break
            
    def sink(self, idx):
        next = idx
        while True:
            if 2*idx+1 < self.size and self.arr[2*idx+1] > self.arr[idx]:
                next = idx*2+1
            if idx*2+2 < self.size and self.arr[2*idx+2] > self.arr[next]:
                next = idx*2+2
            if next == idx:
                break
            else:
                self.arr[next], self.arr[idx] = self.arr[idx], self.arr[next]
                idx = next

    def add_item(self, item):
        self.arr.append(item)
        self.size += 1
        self.swim(self.size-1)

    def empty(self):
        return self.size == 0    

    def del_max(self):
        item = None
        if not self.empty():
            item = self.arr[0]
            self.arr[0] = self.arr[self.size-1]
            self.size -= 1
            self.sink(0)
        return item
        
class TestMaxHeap(unittest.TestCase):
    def setUp(self):
        size = 500
        self.arr = [random.randint(0, size*size) for x in range(size)]

    def test_max_heap(self):
        max_heap = MaxHeap()
        self.assertEqual(max_heap.empty(), True)

        for each in self.arr:
            max_heap.add_item(each)

        test = []
        while not max_heap.empty():
            test.append(max_heap.del_max())
        self.assertListEqual(sorted(self.arr, reverse=True), test)


if __name__ == '__main__':
    unittest.main()
