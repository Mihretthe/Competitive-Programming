from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())
from math import gcd
from collections import defaultdict

def solve():
    n = I()
    a = IL()
    b = IL()
    counter = defaultdict(int)
    count = 0
    
    for i in range(n):
        

        if b[i] == 0:
            if a[i] == 0:
                count += 1
            else:
                counter[0] += 1
            continue
        
        elif a[i] == 0:
            continue
        
        gcdi = gcd(a[i], b[i])

        if -b[i]/a[i] < 0: 
            counter[(-abs(b[i]//gcdi), abs(a[i]//gcdi))] += 1
        else:
            counter[(abs(b[i]//gcdi), abs(a[i]//gcdi))] += 1


    if counter:
        print(max(counter.values()) + count)
    else:
        print(count)
    
 
 
 
T = 1
for _ in range(T):
    solve()