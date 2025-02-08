from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import lcm

def solve():
    n = I()
    a = IL()

    lcmm = (lcm(*a))

    answer = []

    for num in a:
        answer.append(lcmm // num)

    total = sum(answer)
    
    for i, j in zip(a, answer):
        if i * j <= total:
            print(-1)
            return 
    
    print(*answer)

 
 
 
 
T = I()
for _ in range(T):
    solve()