from math import inf
from collections import Counter, defaultdict

class SegmentTree:

    def __init__(self, array):
        self.array = array
        self.length = len(array)
        self.tree = [0] * (2 * self.length)
        self.build()
    
    def build(self):
        for i in range(self.length):
            self.tree[self.length + i] = [self.array[i], 1]

        for i in range(self.length - 1, 0, -1):
            left, lcount = self.tree[2 * i]
            right, rcount = self.tree[2 * i + 1]
            count = 0
            if left == right:
                count = lcount + rcount
            elif left < right:
                count = lcount
            else:
                count = rcount
            self.tree[i] = [min(left, right),count]

        
    def update(self, index, value):
        self.array[index] = value
        index += self.length
        self.tree[index] = [value, 1]

        while index != 1:
            parent = index // 2
            left, lcount = self.tree[2 * parent]
            right, rcount = self.tree[2 * parent + 1]
            count = 0
            if left == right:
                count = lcount + rcount
            elif left < right:
                count = lcount
            else:
                count = rcount
            self.tree[parent] = [min(left, right),count]
            index = parent 


    def query(self, left, right):
        left += self.length
        right += self.length
        counter = defaultdict(int)
        while left < right:
            if left % 2:
                counter[self.tree[left][0]] += self.tree[left][1]
                left = (left + 1) // 2
            else:
                left //= 2

            if right % 2:
                counter[self.tree[right - 1][0]] += self.tree[right - 1][1]
                right = (right - 1) // 2
            else:
                right //= 2
        mini = min(counter)
        return [mini, counter[mini]]


from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, m = II()
    a = IL()
    segment = SegmentTree(a)

    for _ in range(m):
        command, a, b = II()
        if command == 1:
            segment.update(a, b)
        else:
            print(*segment.query(a, b))
 
 
 
 
T = 1
for _ in range(T):
    solve()