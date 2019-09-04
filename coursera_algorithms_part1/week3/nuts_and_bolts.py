import unittest
import random


def partition_array_with_pivot(arr, start, end, pivot):
    if end > start:
        i = start
        j = end
        while True:
            while arr[i] < pivot:
                i += 1
                if i >= end:
                    break
            while arr[j] > pivot:
                j -= 1
                if j <= start:
                    break
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        assert i == j
        return i
    return start


def two_array_sort(arr1, arr2, start, end):
    if end > start:
        pivot = arr2[start]
        k1 = partition_array_with_pivot(arr1, start, end, pivot)
        pivot = arr1[k1]
        k2 = partition_array_with_pivot(arr2, start, end, pivot)
        assert k1 == k2
        two_array_sort(arr1, arr2, start, k1-1)
        two_array_sort(arr1, arr2, k1+1, end)


class TestNutsAndBolts(unittest.TestCase):
    def setUp(self):
        size = 30
        self.nuts = [x for x in range(size)]
        self.bolts = [x for x in range(size)]
        for i in range(size):
            randint = random.randint(0, i)
            self.nuts[i], self.nuts[randint] = self.nuts[randint], self.nuts[i]
            randint = random.randint(0, i)
            self.bolts[i], self.bolts[randint] = self.bolts[randint], self.bolts[i]

    def test_sort(self):
        two_array_sort(self.nuts, self.bolts, 0, len(self.nuts)-1)
        self.assertListEqual(self.nuts, self.bolts)


if __name__ == '__main__':
    unittest.main()
