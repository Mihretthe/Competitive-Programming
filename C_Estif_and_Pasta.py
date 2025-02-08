from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

MOD = 1000000007


def solve():
    k = I()
    

    ans = 6

    num = pow(4, 2**k - 2, MOD)

    print((ans * num) % MOD)

 
 
 
 
T = 1
for _ in range(T):
    solve()