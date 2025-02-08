from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


from heapq import heapify, heappop, heappush

def solve():
    n, m = II()
    graph = {i: 2**i - 1 for i in range(1, n + 1)}
    indegree = {i:i - 1 for i in range(1, n + 1)}
    for _ in range(m):
        u, v = II()
        graph[u] &= ~(1 << v)
        indegree[v] -= 1
    
    deck = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            heappush(deck, -i) 

    answer = []

    while deck:
        node = -heappop(deck)
        for i in graph[node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heappush(deck, -i)

        answer.append(node)
    
    print(*answer)
    

 
 
 
 
T = I()
for _ in range(T):
    solve()