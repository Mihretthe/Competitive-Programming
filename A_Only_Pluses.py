from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from heapq import heappop, heappush, heapify

def solve():
    a = IL()

    heapify(a)
    k = 5
    while k:
        mini = heappop(a)
        mini += 1
        heappush(a, mini)
        k -= 1
    
    b, c, d = a

    print(b * c * d)


 
 
 
 
T = I()
for _ in range(T):
    solve()