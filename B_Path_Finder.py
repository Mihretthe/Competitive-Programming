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

    for _ in range(n - 1):
        u, v, c = II()
        graph[u].append((v, c))
        graph[v].append((u, c))
        maxi = 0
    def dfs(v,w, visited):
        nonlocal ans, maxi
        visited.add(v)
        ans += w
        for i, j in graph[v]:
            if i not in visited:
                visited.add(i)
                dfs(i, j, visited)
                

        maxi = max(maxi, ans)
        ans -= w
        
       


    
    answer = 0

    # print(graph)

    for i in graph[0]:
        v, w = i
        ans = 0
        dfs(v, w, set([0]))
        answer = max(maxi, answer)
        
   
    print(answer)

 
 
 
 
T = 1
for _ in range(T):
    solve()