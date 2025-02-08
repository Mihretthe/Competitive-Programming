from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()

    for i in range(k):
        if n % 10 == 0:
            n /= 10
        else:
            n -= 1
    print(int(n))

	
 
 
 
 
T = 1
for _ in range(T):
    solve()