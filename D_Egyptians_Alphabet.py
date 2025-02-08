from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import gcd, factorial

def comb(num, r):
    return factorial(num) // (factorial(r) * factorial(num - r))


MOD = 1000000007

def calc(a):
    return (pow(a, MOD - 2, MOD)) 
def solve():
    n, m = II()
    s1 = IL()
    s2 = IL()

    ans = 1
    # ans = 0
    index = 0
    for i in range(n):
        a = s1[i]
        b = s2[i]

        if (b != 0 and a > b):
            index = i
            break
        
    for i in range(n):
        a = s1[i]
        b = s2[i]
        
        if (a != 0 and b > a) or (b != 0 and a > b):         
            break
        if (a == 0 and b == 0) or (a != 0 and b != 0):
            continue

        if a == 0:
            neu = m - b 
            if i < index:
                neu += 1
            deno = m
            gc = gcd(neu, deno)
            neu = neu // gc
            deno = deno // gc

            ans *= ((neu % MOD) * calc(deno))  % MOD
            ans %= MOD

        elif b == 0:
            neu = a - 1
            if i < index:
                neu += 1
            
            deno = m
            gc = gcd(neu, deno)
            neu = neu // gc
            deno = deno // gc

            ans *= ((neu % MOD) * calc(deno) % MOD)
            ans %= MOD
        
    
        
    print(ans)

            

 
T = 1
for _ in range(T):
    solve()