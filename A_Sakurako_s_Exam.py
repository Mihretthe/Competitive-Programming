from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    a, b = II()

    if a % 2:
        print("NO")
        return
    
    if b % 2 == 0:
        print("YES")
    else:
        if a > 0:
            print("YES")
        else:
            print("No")
        
 
 
 
T = I()
for _ in range(T):
    solve()