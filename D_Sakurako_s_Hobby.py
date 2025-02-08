from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict
from random import randint

def solve():
    n = I()
    p = IL()
    s = S()
    counter = defaultdict(int)
    x = randint(1, 100)

    parent = {i^x:i^x for i in range(1, n + 1)}

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x


    def union(x, y):
        parentX = find(x)
        parentY = find(y)

        if parentX != parentY:
            parent[parentY] = parentX 

    for i in range(n):
        index, value =(i + 1) ^ x, (p[i]) ^ x
        union(index, value)
    
    for i in range(1, n + 1):
        par = find(i ^ x)
        if s[(i - 1)] == "0":
            counter[par] += 1
    
    answer = [0] * n
    for i in range(n):
        par = find((i + 1) ^ x)
        answer[i] = counter[par]
    
    print(*answer)
 
 
T = I()
for _ in range(T):
    solve()