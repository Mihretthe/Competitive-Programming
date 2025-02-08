from collections import *

n,m,k = map(int, input().split())
parent = { i:i for i in range(1, n+1)}
size = [1]*(n+5)

def find(x):
    while x!=parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(x,y):
    parX = find(x)
    parY = find(y)

    if parX==parY:
        return
    
    if parX in gov:
        parent[parY] = parX
        size[parX]+=size[parY]
    elif parY in gov:
        parent[parX] = parY
        size[parY]+=size[parX]
    elif size[parY]>size[parX]:
        parent[parX] = parY
        size[parY]+=size[parX]
    else:
        parent[parY] = parX
        size[parX]+=size[parY]
    

inDeg = [0]*(n+5)
gov = set(map(int, input().split()))

for _ in range(m):
    ui,vi = map(int, input().split())
    inDeg[ui]+=1
    inDeg[vi]+=1
    union(ui,vi)


maxConnect = -1
mx = max([size[i] for i in gov])

for i in range(1,n+1):
    if size[i]==mx and i in gov:
        maxConnect = i
        break

for i in range(1, n+1):
    if find(i)==i and i not in gov:
        union(i, maxConnect)



ans = 0 

for i in range(1,n+1):
    ans+= size[find(i)]-1-inDeg[i]


print(ans//2)

                                                                                                                                       