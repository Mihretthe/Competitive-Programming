from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, m = II()
    a = IL()
    b = I()
    
    for i in range(n):
        val = b - a[i]
        if i == 0:
            a[i] = max(a[i], val)
        elif val > a[i] and a[i - 1] >= val:
            a[i] = val
        elif a[i - 1] < a[i]:
            a[i] = val
     
    if a == sorted(a, reverse = True):
        print("YES")
    else:
        print("NO")
 
 
 
T = I()
for _ in range(T):
    solve()