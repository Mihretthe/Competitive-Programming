from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()

    
    before = k - 1
    after = n - k

    # print(before, after)
    if before == 0 or after == 0:
        if n == 1:
            print(1)
            print(1)
            
        else:
            print(-1)

        return

    if before % 2 and after % 2:
        print(3)
        print(1, k, k + 1)
    else:
        print(5)
        print(1, 2, k, k + 1, n)
        
 
 
 
T = I()
for _ in range(T):
    solve()