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
    parents = {i:i for i in range(1, n + 1)}
    size = {i:1 for i in range(1, n + 1)}

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(x, y):
        parentX = find(x)
        parentY = find(y)

        if parentX == parentY:
            return parentX

        if parentX != parentY:
            if size[parentX] >= size[parentY]:
                parents[parentY] = parentX
                size[parentX] += size[parentY]
            else:
                parents[parentX] = parentY
                size[parentY] += size[parentX]

    graph = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v, w = II()
        edges.append([u, v, w])
        graph[u].append(v)
        graph[v].append(u)
    
    edges.sort(key = lambda x : x[-1])
    # print(edges)
    weights = defaultdict(lambda : float('inf'))
    ans = defaultdict(list)
    for u, v, w in edges:
        val = union(u, v)
        parent = find(u)
        weights[parent] = min(w,weights[parent])
        if val:
            answer = []
            
            for i in parents:
                if parents[i] == parent:
                    answer.append(i)
            if weights[parent] not in ans:
                ans[weights[parent]] = (weights[parent], u, val)
                
    mini = min(ans.keys())

    b, new, val = ans[mini]
    answer = []
    deck = deque([(new, 0)])
    visited = set([new])

    while deck:
        node, level = deck.popleft()
        if node == val:
            for j, l in deck:
                if l == level:
                    answer.append(j)
                else:
                    break
            break
        
        for i in graph[node]:
            if i not in visited:
                deck.append((i, level + 1))
                visited.add(i)
        answer.append(node)
    print(b, len(answer))
    print(*answer)



            
    
            
    

 
 
T = I()
for _ in range(T):
    solve()
    