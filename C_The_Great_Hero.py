from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil


def solve():
    a, b, n = II()
    arr = IL()
    health = IL()
    arr.sort()
    # print(arr)
    # print(health)
    


    if sum(arr) < b + arr[-1]:
        print("YES")
    else:
        print("NO")
    
 
T = I()
for _ in range(T):
    solve()