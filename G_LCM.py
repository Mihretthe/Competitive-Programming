from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import sqrt, ceil

def solve():
    b = I()
    i = 2
    if b == 1:
        print(1)
        return    

    while i * i <= b:
        if b % i == 0:
            
            break

        i += 1
    else:
        print(2)
        return 
    count = 0
    for i in range(1, int(sqrt(b)) + 1):
        if b % i == 0:
            if b // i == i:
                count += 1
                continue
            count += 2

    print(count)



    
 
 
 
 
T = 1
for _ in range(T):
    solve()