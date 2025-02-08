from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    n, m = II()
    a = [0] + IL()
    parent = {i:i for i in range(1, n + 1)}
    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        parentX = find(x)
        parentY = find(y)

        if a[parentX] <= a[parentY]:
            parent[parentY] = parentX
        else:
            parent[parentX] = parentY
    for _ in range(m):
        u, v = II()
        union(u, v)

    ans = 0
    
    for key, value in parent.items():
        if key == value:
            ans += a[key]
    
    print(ans)
        



 
 
 
 
T = 1
for _ in range(T):
    solve()