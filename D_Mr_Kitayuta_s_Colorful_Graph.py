from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())



def solve():
    n, m = II()
    parent = {j:{i:i for i in range(1, n + 1)} for j in range(1, m + 1)}

    def find(x, c):
        while x != parent[c][x]:
            parent[c][x] = parent[c][parent[c][x]]
            x = parent[c][x]
        return x
        
    def union(x, y, c):
        parentX = find(x, c)
        parentY = find(y, c)

        if parentX != parentY:
            parent[c][parentY] = parent[c][parentX]
        

    for _ in range(m):
        a, b, c = II()
        union(a, b, c)
    
    q = I()
    for _ in range(q):
        u, v = II()
        count = 0
        for i in range(1, m + 1):
            if find(u, i) == find(v, i):
                count += 1
        print(count)


    
 
 
 
 
T = 1
for _ in range(T):
    solve()