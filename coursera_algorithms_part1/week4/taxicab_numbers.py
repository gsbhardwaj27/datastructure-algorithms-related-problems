# taxicab_numbers with O(n2) time and
# O(n2) space complexity
def taxicab_numbers(n):
    taxi_cabs = set()
    for i in range(1, n):
        for j in range(i, n):
            num = i**3 + j**3
            if num in taxi_cabs:
                print(num)
            else:
                taxi_cabs.add(num)


# taxicab_numbers with O(n2) time and
# O(n) space complexity
class MaxPQ:
    def __init__(self, n):
        self.arr = [None for x in range(n)]
        self.size = 0

    def swim(self, idx):
        while idx > 0 and self.arr[(idx-1)//2] < self.arr[idx]:
            self.arr[(idx-1)//2], self.arr[idx] = self.arr[idx], self.arr[(idx-1)//2]
            idx = (idx-1)//2

    def sink(self, idx):
        while idx*2 + 1 < self.size:
            mx_idx = idx*2 + 1
            if 2*idx + 2 < self.size and self.arr[2*idx + 2] > self.arr[2*idx + 1]:
                mx_idx = 2*idx + 2
            if self.arr[mx_idx] > self.arr[idx]:
                self.arr[mx_idx], self.arr[idx] = self.arr[idx], self.arr[mx_idx]
                idx = mx_idx
            else:
                break

    def add_item(self, val):
        self.arr[self.size] = val
        self.swim(self.size)
        self.size += 1

    def delMax(self):
        if self.size > 0:
            val = self.arr[0]
            self.arr[0] = self.arr[self.size-1]
            self.size -= 1
            self.sink(0)
            return val
  
    def get_size(self):
        return self.size


def taxicab_numbers_better(n):
    mpq = MaxPQ(n)
    last = None
    temps = []
    temps_in = []
    for i in range(n, 0, -1):
        for j in range(n, n-i, -1):
            # print(mpq.arr)
            num = i**3 + j**3
            temps_in.append(num)
            if mpq.size < n:
                mpq.add_item(num)
            else:
                curr = mpq.delMax()
                #print(curr)
                if curr == last:
                    print(curr)
                last = curr
                mpq.add_item(num)
        temps.append(temps_in)
        temps_in = []
    while mpq.size > 0:
        curr = mpq.delMax()
        if curr == last:
            print(curr)
        last = curr
    #from pprint import pprint
    #pprint(temps)


print(taxicab_numbers_better(15))
print(taxicab_numbers(15))
