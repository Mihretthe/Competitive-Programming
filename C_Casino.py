from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import lcm, gcd, log

def solve():
    length = I()
    a = IL()
    
    for i in range(length):
        num = a[i]

        while num > 1 and  num % 2 == 0:
            num //= 2
        
        while num > 1 and  num % 3 == 0:
            num //= 3
        
        a[i] = num

    if len(set(a)) == 1:
        print("Yes")
    else:
        print("No")
        






 
T = 1
for _ in range(T):
    solve()