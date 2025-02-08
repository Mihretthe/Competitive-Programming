from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()
    prefix = [-k] * (10)

    for _ in range(n):
        l, r, p = II()
        prefix[r] += p

    print(prefix)
        
        


 
 
 
 
T = 1
for _ in range(T):
    solve()