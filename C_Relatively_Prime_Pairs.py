from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    l, r = II()
    print("YES")
    for i in range(l, r + 1, 2):
        print(i, i + 1)
    


 
 
 
 
T = 1
for _ in range(T):
    solve()