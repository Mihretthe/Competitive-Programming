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
    deck = deque()
    parents = defaultdict(int)

    for _ in range(n - 1 + m):
        u, v = II()
        graph[u].append(v)
        indegree[v] += 1

    for i in range(1, n + 1):
        if i not in indegree:
            deck.append(i)
    

    while deck:
        node = deck.popleft()

        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                parents[i] = node
                deck.append(i)
   
    for i in range(1, n + 1):
        print(parents[i])
    


 
 
 
 
T = 1
for _ in range(T):
    solve()