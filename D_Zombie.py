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

    for _ in range(m):
        u, v = II()
        graph[u].append(v)
        graph[v].append(u)

    
    deck = deque([(1, 0)])
    visited = set([1])

    ruq = (1, 0)

    while deck:
        node, length = deck.popleft()

        for friend in graph[node]:
            if friend not in visited:
                deck.append((friend, length + 1))
                visited.add(friend)
        ruq = (node, length)

    deck = deque([(ruq[0], 0)])
    visited = set([ruq[0]])

    ruq1 = (ruq[0], 0)

    while deck:
        node, length = deck.popleft()

        for friend in graph[node]:
            if friend not in visited:
                deck.append((friend, length + 1))
                visited.add(friend)
        ruq1 = (node, length)
    
    print(max(ruq[1], ruq1[1]))




            


    


 
 
 
 
T = 1
for _ in range(T):
    solve()