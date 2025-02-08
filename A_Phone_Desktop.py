from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def solve():
    x, y = II()

    if y:
        if y % 2:
            for_y = (y // 2) 
            remain = (for_y * 15) - ((y - 1) * 4)
            for_y += 1
            remain += 11
            x -= remain
            print(for_y + max(0, ceil(x / 15)))
        else:
            for_y = (y // 2) 
            remain = (for_y * 15) - ((y) * 4)
            x -= remain
            print(for_y + max(0, ceil(x / 15)))
    else:
        print(ceil(x / 15))
 
 
 
T = I()
for _ in range(T):
    solve()