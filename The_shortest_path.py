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
    start, end = II()
    graph = defaultdict(list)

    for _ in range(m):
        u, v = II()
        graph[u].append(v)
        graph[v].append(u)
    
    deck = deque([start])
    current = {-1 : start}
    while deck:
        node = deck.popleft()
        for i in graph[node]:
            if i not in  current:
                current[i] = node                
                deck.append(i)
                    



    path = [end]

    while end in current:
        end = current[end]
        path.append(end)
        if start == end:
            print(len(path) - 1)
            print(*path[::-1])
            break
    else:
        print(-1)
    
 
 
T = 1
for _ in range(T):
    solve()