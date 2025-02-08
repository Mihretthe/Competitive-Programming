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
            self.tree[i] = self.tree[i * 2] + self.tree[2 * i + 1]
        

    def update(self, index):
        self.array[index] ^= 1
        index += self.length
        self.tree[index] ^= 1

        while index != 1:
            parent = index // 2
            self.tree[parent] = self.tree[parent * 2 + 1] + self.tree[parent * 2]
            index = parent


    def query(self, k, parent):
        if parent >= self.length:
            return parent - self.length
        
        if self.tree[parent] == k:
            print("parent: ",parent, self.tree[parent])
            return calc(parent, self.length)
        elif self.tree[parent] > k:
            return self.query(k, parent * 2)
        else:
            return self.query(k, parent * 2 + 1)
    
        
        


from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def calc(index, length):
    while index < length:
        index = 2 * index
    return index - length

def solve():
    n, m = II()
    a = IL()

    segment = SegmentTree(a)
    print(segment.tree)

    for _ in range(m):
        command, k = II()
        if command == 1:
            segment.update(k)
        else:
            k += 1
            print(segment.query(k, 1))
    
    
    
 
 
 
 
T = 1
for _ in range(T):
    solve()