import unittest
import random
from collections import Counter


def three_way_partition(arr, start, end, dominants):
    if (end - start + 1) >= int(len(arr)/10):
        lt = start
        gt = end
        i = lt
        while True:
            if arr[i] < arr[lt]:
                arr[lt], arr[i] = arr[i], arr[lt]
                i += 1
                lt += 1
            elif arr[i] > arr[lt]:
                arr[gt], arr[i] = arr[i], arr[gt]
                gt -= 1
            else:
                i += 1
            if i > gt:
                break
        if gt - lt + 1 > int(len(arr)/10):
            dominants.append(arr[lt])
        three_way_partition(arr, start, lt-1, dominants)
        three_way_partition(arr, gt + 1, end,  dominants)


def decimal_dominants(arr):
    dominants = []
    three_way_partition(arr, 0, len(arr)-1, dominants)
    return dominants


class TestDecimalDominants(unittest.TestCase):
    def setUp(self):
        size = 1000
        self.arr = [random.randint(0, size/100) for x in range(size)]

    def test_decimal_dominants(self):
        counter = Counter(self.arr)
        dominants = sorted([x for x in counter.keys() if counter[x] > int(len(self.arr)/10)])
        self.assertListEqual(sorted(decimal_dominants(self.arr)),
                             dominants)


if __name__ == '__main__':
    unittest.main()
