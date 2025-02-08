from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    ans = {1:400, 2:300, 3:200, 4:150, 5:100}
 
    n = I()
    if n not in ans:
        print(0)
    else:
        print(ans[n])
 
 
T = I()
for _ in range(T):
    solve()