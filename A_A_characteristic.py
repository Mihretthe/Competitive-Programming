from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def calc(n):
    return (n * (n - 1)) // 2
def solve():
    n, k = II()
    for i in range(n):
        a = i 
        b = n - i
        if k == calc(a) + calc(b):
            print("YES")
            ans = ([1] * a + [-1] * (b))
            print(*ans)
            return 
    else:
        print("NO")


    
    

 
 
T = I()
for _ in range(T):
    solve()