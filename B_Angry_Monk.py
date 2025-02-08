from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()
    a = IL()
    maxi = max(a)
    total = sum(a)

    total -= maxi
    a.remove(maxi)

    for num in a:
        total += (num - 1)
    
    print(total)
 
 
 
 
T = I()
for _ in range(T):
    solve()