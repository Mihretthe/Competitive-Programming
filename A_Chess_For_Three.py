from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from heapq import heapify, nlargest

def solve():
    array = IL()
    count = 0
    
    while array[1] != 0 and array[2] != 0:
        array[1] -= 1
        array[2] -= 1
        array.sort()
        count += 1
    if array[0] == 0 and array[1] == 0 and array[2] % 2 == 0:
        print(count)
    else:
        print(-1)


 
 
 
T = I()
for _ in range(T):
    solve()