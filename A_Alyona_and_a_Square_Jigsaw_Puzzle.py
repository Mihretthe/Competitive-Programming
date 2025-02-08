from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import sqrt

def solve():
    n = I()
    a = IL()

    prefix = [a[0]]

    for num in a[1:]:
        prefix.append(prefix[-1] + num)

    count = 0
    
    for i in range(n):
        sq = sqrt(prefix[i])
        if sq.is_integer() and sq % 2:
            count += 1
    
    print(count)
 
 
 
 
T = I()
for _ in range(T):
    solve()