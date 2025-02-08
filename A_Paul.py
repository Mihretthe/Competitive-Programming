from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

def solve():
    s = S()
    counter = defaultdict(int)

    for i in s:
        if counter[i] < 2:
            counter[i] += 1
    
    total = sum(counter.values())

    print(total // 2)




 
 
 
 
T = I()
for _ in range(T):
    solve()