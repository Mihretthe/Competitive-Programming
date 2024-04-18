from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())
from collections import defaultdict, Counter





def solve():
    n, m = II()
    graph  = defaultdict(int)

    for _ in range(m):
        u, v = II()
        graph[u] += 1
        graph[v] += 1
    counter = Counter(graph.values()) 

    def bus():
        return counter[1] == 2 and len(counter) == 2 and 2 in counter
    
    def ring():
        return len(counter) == 1  and 2 in counter

    def star():
        return len(counter) == 2 and 1 in counter and n - 1 in counter and 1 in counter

    if bus():
        print("bus topology")
    elif ring():
        print("ring topology")
    elif star():
        print("star topology")
    else:
        print("unknown topology")
    

 
T = 1
for _ in range(T):
    solve()