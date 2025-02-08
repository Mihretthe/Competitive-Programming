from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict, Counter

def solve():
    n, k = II()

    s = list(S())

    parent = {i:i for i in range(n)}
    size = {i:1 for i in range(n)}

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x


    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if size[rootX] > size[rootY]:
                parent[rootY] = rootX
                size[rootX] += size[rootY]
            else:
                parent[rootX] = rootY
                size[rootY] += size[rootX]


    
    for i in range(n):        
        union(i, n - i - 1)
        if i + k < n:
            union(i, i + k)
    
    
    count = 0
    
    hashmap = defaultdict(list)
    for key, value in parent.items():
        hashmap[value].append(s[key])

   

    for key, value in hashmap.items():
        counter = Counter(value)
        maxi = max(counter.values())

        count += len(value) - maxi

    print(count)



 
T = I()
for _ in range(T):
    solve()