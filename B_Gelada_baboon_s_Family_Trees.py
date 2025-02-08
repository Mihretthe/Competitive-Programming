from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())



def solve():
    n = I()
    p = [0] + IL()

    parents = {i:i for i in range(1, n + 1)}

    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(x, y):
        parentX = find(x)
        parentY = find(y)

        if parentX != parentY:
            parents[parentY] = parentX


    for i in range(1, n + 1):
        union(i, p[i])
    
    count = 0
    for i in parents:
        if i == parents[i]:
            count += 1
        
    print(count)



 
 
 
 
T = 1
for _ in range(T):
    solve()