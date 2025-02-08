from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import log2

def solve():
    n = I()
    count = 0
    if n == 1:
        print(0)
        return 
    if n % 2 == 0:
        n = (n // 2) 
        count += 1
        if  log2(n) == int(log2(n)):
            print(int(count + log2(n)))
            return
    
    while n % 5 == 0:
        n = (n // 5) * 4
        count += 1
        if  log2(n) == int(log2(n)):
            print(int(count + log2(n)))
            return 
        
    while n % 3 == 0:
        n = (n // 3) * 2
        count += 1
        if  log2(n) == int(log2(n)):
            print(int(count + log2(n)))
            return

      
    print(-1)
 
 
 
T = I()
for _ in range(T):
    solve()