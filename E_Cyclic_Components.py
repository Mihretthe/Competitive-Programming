from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    n, m = II()
    graph = defaultdict(list)

    for _ in range(m):
        u, v = II()
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    
    
    def dfs(node, path):
        stack = [node]
        while stack:
            node = stack.pop()
            visited[node] = True
            path.append(node)
            for i in graph[node]:
                if not visited[i]:
                    stack.append(i)
        return path

    components = []

    for i in range(1, n + 1):
        if len(graph[i]) == 2 and not visited[i]:
            components.append(dfs(i, []))
    
    count = 0

    for tree in components:
        for i in tree:
            if len(graph[i]) != 2:
                break
        else:
            count += 1
    
    print(count)



 
 
 
T = 1
for _ in range(T):
    solve()