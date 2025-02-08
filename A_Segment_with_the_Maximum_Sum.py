
class SegmentTree:
    def __init__(self, array):
        self.array = array
        self.length = len(array)        
        self.tree = [0] * (2 * self.length)
        self.build()
    
    def build(self):
        for i in range(self.length):
            self.tree[i + self.length] = self.array[i]
        
        for i in range(self.length - 1, 0, -1):
            left = 2 * i
            right = 2 * i + 1
            self.tree[i] = self.tree[left] + self.tree[right]

    def update(self, index, value):
        self.array[index] = value
        index += self.length
        self.tree[index] = value
        # self.maxi = max(self.maxi, value)
        
        while index != 1:
            i = index // 2
            left = 2 * i
            right = 2 * i + 1
            self.tree[i] = self.tree[left] + self.tree[right]
            index = i

    def query(self):
        # print(self.tree)
        return max(self.tree[1:])
    # def query(self, left, right):
    #     left += self.length
    #     right += self.length
    #     maxi = 0
    #     while left < right:
    #         if left % 2:
    #             maxi = max(maxi, self.tree[left])
    #             left += 1

    #         if right % 2:
    #             maxi = max(maxi, self.tree[right - 1])
    #             right -= 1
            
    #         left //= 2
    #         right //= 2

    #     return maxi

    
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
    

    print(segment.query())
    for _ in range(m):
        i, v = II()
        segment.update(i, v)
        print(segment.query())
       
 
 
 
T = 1
for _ in range(T):
    solve()