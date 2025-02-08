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
    array = []

    for _ in range(n):
        c, t = II()
        if array:
            array.append(array[-1] + c * t)
        else:
            array.append(c * t)
    
    v = IL()

    for num in v:
        print(bisect_left(array, num) + 1)
 
 
 
 
T = 1
for _ in range(T):
    solve()