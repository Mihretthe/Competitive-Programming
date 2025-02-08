from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

parents = {}

class DSU:
    def __init__(self, size):
        self.size = size
        self.parents = {i:i for i in range(1, size + 1)}
        self.mini = {i:i for i in range(1, size + 1)}
        self.maxi = {i:i for i in range(1, size + 1)}
        self.count = defaultdict(lambda : 1)
        

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            self.parents[parentY] = parentX        
            self.mini[parentX] = min(self.mini[parentY],self.mini[parentX])
            self.maxi[parentX] = max(self.maxi[parentY], self.maxi[parentX])
            self.count[parentX] += self.count[parentY]
            
    def find(self, x):
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    
    

def solve():
    n, m = II()
 
    dsu = DSU(n)
    for _ in range(m):
        command = SL()
        if len(command) == 2:
            belong = dsu.find(int(command[1]))
            print(dsu.mini[belong], dsu.maxi[belong], dsu.count[belong])
        else:
            dsu.union(int(command[1]), int(command[2]))
            

T = 1
for _ in range(T):
    solve()