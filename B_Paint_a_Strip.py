from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import log2, ceil

generated_array = [1, 4, 10, 22, 46, 94, 190, 382, 766, 1534, 3070, 6142, 12286, 24574, 49150, 98302]

from bisect import bisect_left
def solve():
    n = I()
    index = (bisect_left(generated_array, n))
    print(index + 1)

    
 
 
 
 
T = I()
for _ in range(T):
    solve()