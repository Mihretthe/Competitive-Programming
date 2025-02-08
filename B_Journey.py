from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, a, b, c = II()
    total = sum((a, b, c))
    mod = n % total
    days = n // total

    # print(days, mod)

    if mod == 0:
        print(days * 3)
    else:
        mod -= a
        if mod <= 0:
            print(days * 3 + 1)
        else:
            mod -= b
            if mod <= 0:
                print(days * 3 + 2)
            else:
                print(days * 3 + 3)

 
 
 
T = I()
for _ in range(T):
    solve()