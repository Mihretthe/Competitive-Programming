from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    graph = defaultdict(list)
    n = I()

    for _ in range(n - 1):
        u, v = II()
        graph[v].append(u)
    init = IL()
    goal = IL()
    answer = []
    stack = [1]
    level = 1
    flipped = False
    deck = []
    while stack:
        node = stack.pop()
        if init[node - 1] != goal[node - 1]:
            answer.append(node)
            flipped = True
            deck.append([level % 2, flipped])
        level += 1
        stack.extend(graph[node])
    print(graph)




    
 
 
 
 
T = 1
for _ in range(T):
    solve()