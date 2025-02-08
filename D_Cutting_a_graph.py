from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, m, k = II()
    edges = set()
    parent = {i:i for i in range(1, n + 1)}
    size = {i:1 for i in range(1, n + 1)}

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        parentX = find(x)
        parentY = find(y)

        if parentX != parentY:
            if size[parentX] >= size[parentY]:
                parent[parentY] = parentX
                size[parentX] += size[parentY]
            else:
                parent[parentX] = parentY
                size[parentY] += size[parentX]
    
    
    

    for _ in range(m):
        u, v = II()
        edges.add((u, v))

    queries = []
    
    for _ in range(k):
        type, u, v = S().split()
        u, v = int(u), int(v)

        if type == "cut":
            edges.discard((u, v))
            edges.discard((v, u))
        queries.append((type, u, v))
            

    for u, v in edges:
        union(u, v)   
      
                
    answer = []

    for type, u, v in queries[::-1]:
        if type == "ask":
            if find(u) == find(v):
                answer.append("YES")
            else:
                answer.append("NO")
        else:
            union(u, v)

 
    for ans in answer[::-1]:
        print(ans)
 
 
T = 1
for _ in range(T):
    solve()