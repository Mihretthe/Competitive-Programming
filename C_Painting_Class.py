from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict, deque

def solve():
    n = I()
    edges = IL()
    colors = IL()
    
    graph = defaultdict(list)

    for i in range(n - 1):
        graph[edges[i]].append(i + 2)
    
    # print(graph)

    deck = deque([(1, colors[0])])
    count = 1
    while deck:
        node, color = deck.popleft()
        if color != colors[node - 1]:
            count += 1
            color = colors[node - 1]
        for i in graph[node]:
            deck.append((i, color))
    
    print(count)

    

 
 
 
 
T = 1
for _ in range(T):
    solve()