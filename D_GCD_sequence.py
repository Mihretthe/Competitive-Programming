from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import gcd

def solve():
    n = I()
    a = IL()
    pre = []
    suff = []

    for i in range(n - 1):
        pre.append(gcd(a[i], a[i + 1]))

    for i in range(n - 1, 0, -1):
        suff.append(gcd(a[i], a[i - 1]))

    suff = suff[::-1]

    count = 0

    for i in range(n - 2):
        if pre[i] > pre[i + 1]:
            count += 1
        
    # print(count)

    if count <= 1:
        print("YES")
    else:
        print("NO")
        



    
 
 
 
 
T = I()
for _ in range(T):
    solve()
    # print()