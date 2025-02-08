from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n , q = II()

    parent = {i:i for i in range(1, n + 1)}
    neighbour = {i: i + 1 for i in range(1, n + 1)}

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    
    def union(x, y):
        parentX = find(x)
        parentY = find(y)

        if not isConnected(parentX, parentY):
            parent[parentY] = parentX
            


        
    def isConnected(x, y):
        return find(x) == find(y)
    

    for _ in range(q):
        type, x, y = II()
        if type == 1:
            union(x, y)
        elif type == 2:
            nx = neighbour[x] 
            while nx <= y:
                union(x, nx)
                temp = neighbour[nx]
                neighbour[nx] = neighbour[y]
                nx = temp



            
        else:
            if isConnected(x, y):
                print("YES")
            else:
                print("NO")

        

 
 
 
T = 1
for _ in range(T):
    solve()