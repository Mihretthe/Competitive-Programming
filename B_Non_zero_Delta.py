from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, a, b = II()
    if b >= 0:
        val = (a + b) % n
        if val == 0:
            val = n
        print(val)
    else:
        b = -b
        if b < a:
            print((a - b))
        elif b > a:
            b -= a
            val = (n - b) % n
            if val == 0:
                val = n
            print(val)
        else:
            print(n)
 
 
 
 
T = 1
for _ in range(T):
    solve()