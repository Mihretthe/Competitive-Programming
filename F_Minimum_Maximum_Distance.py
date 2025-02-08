from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    n, k = II()
    marked = set(IL())

    graph = defaultdict(list)

    for _ in range(n - 1):
        u, v = II()
        graph[u].append(v)
        graph[v].append(u)
    
    print(graph)

 
 
 
 
T = I()
for _ in range(T):
    solve()