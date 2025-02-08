from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import factorial


def solve():
    answer = 1
    a = list(map(int, list(input())))
    n = len(a)
    count = 0
    curr = a[0]
    op = 0
    end = False
    MOD = 998244353

    for i in range(n):
        if a[i] == curr:
            count += 1
            end = True
        else:
            end = False
            op += (count - 1)
            answer *= factorial(count)
            answer %= MOD
            count = 1
            curr = a[i]
            
    if end:
        op += (count - 1)
        answer *= factorial(count)
        answer %= MOD
    

    print(op, answer)

 
 
T = I()
for _ in range(T):
    solve()





