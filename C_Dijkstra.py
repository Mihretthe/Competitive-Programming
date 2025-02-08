from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict, deque
from heapq import heappop, heappush
from math import inf

def solve():
    n, m = II()
    graph = defaultdict(list)

    for _ in range(m):
        u, v, w = II()
        if u == v:
            continue
        graph[u].append((w, v))
        graph[v].append((w, u))

    table = [inf] * (n + 1)
    table[1] = 0
    parent = {1:1}

    heap = [(0, 1)]
    processed = set()
    answer = []

    while heap:
        weight, node = heappop(heap)
        
        if node in processed:
            continue
        answer.append(node)
        if node == n:
            break
        for w, friend in graph[node]:
            if friend not in processed:
                if table[friend] > w + weight:
                    parent[friend] = node
                table[friend] = min(table[friend], w + weight)
                heappush(heap, (table[friend], friend))
        
        processed.add(node)
    
    # print(table)
    # print(answer)
    # print(processed)

    # print(parent)
    if table[n] == inf:
        print(-1)
        return

    answer = deque()
    node = n
    while node != 1:
        answer.appendleft(node)
        node = parent[node]
    answer.appendleft(1)
    print(*answer)



            




    


 
 
 
 
T = 1
for _ in range(T):
    solve()