from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict, deque

def solve():
    S()
    n, k = II()
    friends = IL()
    graph = defaultdict(list)
    

    for _ in range(n - 1):
        u, v = II()
        graph[u].append(v)
        graph[v].append(u)
    
    
    deck = deque([(1, True)])
    visited = set([1])
    for i in friends:
        deck.appendleft((i, False))
        visited.add(i)
    
    while deck:
        node, vlad = deck.popleft()
        if vlad and len(graph[node]) == 1 and node != 1:
            print("YES")
            break
        for i in graph[node]:
            if i not in visited:
                deck.append((i, vlad))
                visited.add(i)
    else:
        print("NO")
 
T = I()
for _ in range(T):
    solve()