def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

def S() : return input()

def SL() : return list(input().split())

from math import ceil
 
def solve():
    n = I()
    a = IL()

    a.sort()
    index = ceil(n / 2) - 1
    num = a[index]

    a = a[index:]

    print(a.count(num))
 
 
 
 
T = I()
for _ in range(T):
    solve()