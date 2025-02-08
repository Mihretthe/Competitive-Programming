from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    four = n // 4

    n = n % 4
    if n == 0:
        print(four)
    elif n == 1:
        if four < 2:
            print(-1)
        else:
            print(four - 1)
    elif n == 2:
        if four < 1:
            print(-1)
        else:
            print(four)
    else:
        if four < 3:
            print(-1)
        else:
            print(four - 1)
 
 
T = I()
for _ in range(T):
    solve()