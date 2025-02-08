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
            print(segment.query(a, b))


 
 
 
 
T = 1
for _ in range(T):
    solve()


