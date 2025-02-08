from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_left

def solve():
    n, m = II()
    a = IL()
    b = IL()
    sorted_a = sorted(a)
    many = []

    for i in range(m):
        num = b[i]
        index = bisect_left(sorted_a, num)
        many.append(n - index)
    
    array = []

    for i in range(m):
        array.append((b[i], many[i]))
    
    array.sort(key = lambda x : x[1])

    for i in range(1, m + 1):
        





 
 
 
 
T = I()
for _ in range(T):
    solve()