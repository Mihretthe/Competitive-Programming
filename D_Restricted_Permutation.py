from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict, deque
from heapq import heappush, heappop, heapify

def solve():
    n, m = II()
    graph = defaultdict(list)
    indegree = defaultdict(int)
    deck = set(range(1, n + 1))
    for _ in range(m):
        u, v = II()
        graph[u].append(v)
        indegree[v] += 1
        deck.discard(v)

    answer = []

    deck = list(deck)
    heapify(deck)
    while deck:
        node = heappop(deck)
        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heappush(deck, i)
        answer.append(node)

    

    if len(answer) == n:
        print(*answer)
    else:
        print(-1)



 
 
 
 
T = 1
for _ in range(T):
    solve()