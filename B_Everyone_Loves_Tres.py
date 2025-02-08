from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()

    if n % 2 == 0:
        ans = ["3"] * (n - 2)
        ans.append("66")
        print("".join(ans))
    else:
        if n < 5:
            print(-1)
        else:
            ans = ["3"] * (n - 5)
            ans.append("36366")
            print("".join(ans))
 
 
 
 
T = I()
for _ in range(T):
    solve()