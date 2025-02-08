from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter

def solve():
    n = I()
    a = IL()


    odd = 0
    even = 0

    c_odd = 0
    c_even = 0

    for i in range(n):
        if i % 2:
            odd += a[i]
            c_odd += 1
        else:
            even += a[i]
            c_even += 1
    
    if odd % c_odd == 0 and even % c_even == 0 and odd // c_odd == even / c_even:
        print("YES")
    else:
        print("NO")



    
 
 
 
 
T = I()
for _ in range(T):
    solve()