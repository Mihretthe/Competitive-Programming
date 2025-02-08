from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    a, b, c, d = II()
    
    ans = 0
    
    if a > c and b > d:
        ans += 2
    if a > d and b > c:
        ans += 2
    if b > c and a == d:
        ans += 2
    if b > d and a == c:
        ans += 2
    if a > c and b == d:
        ans += 2
    if a > d and b == c:
        ans += 2
    
    
    print(ans)
 
 
 
 
T = I()
for _ in range(T):
    solve()
    
    
    
    
"""

Baby

eyba
byyt
baby


"""