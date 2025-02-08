from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict, deque

def solve():
    n = I()
    
    parents = {i:i for i in range(1, n + 1)}
    size = {i:1 for  i in range(1, n + 1)}


    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(x, y):
        parentX = find(x)
        parentY = find(y)

        if parentX != parentY:
            if size[parentX] >= size[parentY]:
                parents[parentY] = parentX
                size[parentX] += size[parentY]
                graph[parentX].extend(graph[parentY])
            else:
                parents[parentX] = parentY
                size[parentY] += size[parentX]
                graph[parentY].extend(graph[parentX])

    graph = {i:[i] for i in range(1, n + 1)}
    for _ in range(n - 1):
        u, v = II()
        union(u, v)

    

    for i in range(1, n + 1):
        if i == parents[i]:
            print(*graph[i])
            return
    
    



    


 
 
 
 
T = 1
for _ in range(T):
    solve()