from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from heapq import heapify, heappop, heappush

def solve():
    n = I()
    s = IL()
    s = list(map(lambda x : -x, s))
    heap = []
    
    answer = 0
    for i in range(n):
        if s[i] == 0:
            if heap:
                answer += heappop(heap)
        else:
            heappush(heap, s[i])
    
    print(-answer)


 
 
 
 
T = I()
for _ in range(T):
    solve()