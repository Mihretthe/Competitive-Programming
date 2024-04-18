from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict


def solve():
    n = I()
    if n == 1:
        print(0)
        return 
    graph = defaultdict(list)
    for _ in range(n - 1):
        u, v = II()
        graph[u].append(v)
        graph[v].append(u)
    color = [-1] * n

    stack = [1]
    visited = set()

    while stack:
        node = stack.pop() 
        if color[node - 1] == -1 or color[node - 1] == 0:
            color[node - 1] = 0
            for i in graph[node]:
                color[i - 1] = 1
                if i not in visited:
                    stack.append(i)
                    visited.add(i)
        elif color[node - 1] == 1:
            for i in graph[node]:
                color[i - 1] = 0
                if i not in visited:
                    stack.append(i)
                    visited.add(i)

    print(color.count(1) * color.count(0) - n + 1) 
 
 
T = 1
for _ in range(T):
    solve()