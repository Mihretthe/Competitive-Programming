from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from heapq import heapify, heappop, heappush

def solve():
    n, k, q = II()
    t = IL()
    heap = []

    for _ in range(q):
        i, f = II()
        if i == 1:
            heappush(heap, (t[f-1], f))
            if len(heap) > k:
                heappop(heap)
        else:
            if (t[f-1], f)in heap:
                print("YES")
            else:
                print("NO")


 
 
 
 
T = 1
for _ in range(T):
    solve()