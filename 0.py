from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    a = IL()
    b = IL()
    count = a[-1]
    for i in range(n - 1):
        
        count += max(a[i] - b[i + 1], 0)
    
    print(count)
 
 
 
T = I()
for _ in range(T):
    solve()
    






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
            self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i]
        
        
    def update(self, index, value):
        index = self.length + index
        self.tree[index] = value
        
        while index != 1:
            parent = index // 2
            
            self.tree[parent] = self.tree[parent * 2] + self.tree[parent * 2 + 1]
            index = parent
    
    def query(self, left, right):
        left += self.length
        right += self.length

        answer = 0
        
        while left < right:
            if left % 2:
                answer += self.tree[left]
                left = (left + 1) // 2
            else:
                left //= 2
            if right % 2:
                answer += self.tree[right - 1]
                right = (right - 1) // 2
                
            else:
                right //= 2
    
        return answer
    
    
def KMP_part_one(p : str) -> list:
    m = len(p)
    i , j = 0, 1
    LPS = [0 for _ in range(m)]
    while j < m:
        if p[i] == p[j]:
            LPS[j] = i + 1
            i += 1
            j += 1
        else:
            if i == 0:
                j += 1
            else:
                i = LPS[i - 1]
    return LPS

class Solution:
    def strStr(self, haystack: str, needle: str, n, m) -> int:
        LPS = KMP_part_one(needle)
        i, j = 0, 0
        while j < n:
            if needle[i] == haystack[j]:
                i += 1
                j += 1
            else:
                if i == 0:
                    j += 1
                else:
                    i = LPS[i - 1]
            if i >= m:
                return j - m
        return -1

 
        
        
    
