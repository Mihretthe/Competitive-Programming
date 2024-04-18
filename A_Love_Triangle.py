from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(lambda x : int(x) - 1, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()))

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def dfs(vertex, visited, graph):
    stack = [(vertex, 0)]
    visited[vertex] = 1
    ans = 0
    start = -1
    i = 0

    while stack:
        node, state = stack.pop()
        if i and graph[node] in visited and visited[graph[node]]:
            start = graph[node]
            break
        i += 1

        if state:
            visited[node] = 0
            continue
            
        stack.append((node, 1))

        if graph[node] not in visited:
            stack.append((graph[node], 0))
            visited[node] = 1

    if start > -1:
        for node in stack:
            visited[node] = 0
        for node in visited:
            visited[node] = 0
        
        
        while stack and start != stack[-1][0]:
            ans += 1
            stack.pop()
    
    return ans == 1
        
def solve():
    n = I()
    graph = IL()
    visited = {}

    for vertex in range(len(graph)):
        if vertex not in visited:
            if dfs(vertex, visited, graph):
                print("YES")
                return
    print("NO")

    
T = 1
for _ in range(T):
    solve()