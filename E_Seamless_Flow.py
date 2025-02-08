from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict, deque

def solve():
    n, m = II()
    graph = defaultdict(list)
    indegree = defaultdict(int)
    undirected = []
    count = m
    for _ in range(m):
        t, u, v = II()
        if t:
            graph[u].append(v)
            indegree[v] += 1
        else:
            undirected.append((u, v))
            count -= 1

    deck = deque()
    for i in range(1, n + 1):
        if not indegree[i]:
            deck.append(i)
    topsort = defaultdict(int)
    num = 0
    while deck:
        node = deck.popleft()
        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                deck.append(i)
        topsort[node] = num
        num += 1
    if len(topsort) < n:
        print("NO")
        return 

    for u, v in undirected:
        if topsort[u] < topsort[v]:
            graph[u].append(v)
        else:
            graph[v].append(u)
    print("YES")
    for node in graph:
        for j in graph[node]:
            print(node, j)
 
 
 
T = I()
for _ in range(T):
    solve()