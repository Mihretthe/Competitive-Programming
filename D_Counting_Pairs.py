from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_right, bisect_left

def solve():
    n, x, y = II()
    a = IL()

    a.sort()

    total = sum(a)

    if total <= x:
        print(0)
        return

    count = 0
    for i in range(n):
        num = a[i]
        index2 = bisect_left(a, total - num - y ,lo=i + 1, hi=n)
        index = bisect_right(a, total - num - x ,lo=i + 1, hi=n)
        count += max(0, index - index2)

    print(count)

    
    
 
 
T = I()
for _ in range(T):
    
    solve()