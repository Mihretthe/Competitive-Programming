from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_left, bisect_right

def solve():
    n, l, r, k = II()
    a = IL()

    a.sort()

    count = 0
    running = 0

    for i in range(n):
        if a[i] < l:
            continue
        if a[i] > r:
            break
        running += a[i]
        if running > k:
            break
        count += 1
    
    print(count)
        

    
 
 
 
T = I()
for _ in range(T):
    solve()