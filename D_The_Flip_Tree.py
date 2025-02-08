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
    graph = defaultdict(list)
    deck = deque()

    for _ in range(n):
        u, v = II()
        graph[v].append(u)
    
    init = [0] + IL()
    goal = [0] + IL()

    deck.append((1, False, False))

    while deck:
        node, parent, grand = deck.popleft()

        for i in graph[node]:
            pass




    





    
 
 
 
 
T = 1
for _ in range(T):
    solve()