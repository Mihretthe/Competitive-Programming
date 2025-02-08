from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())



def solve():
    b, c, d = II()
    ans = 0

    for i in range(62):
        num = 1 << i 
        _b = int(bool(num & b))
        _c = int(bool(num & c))
        _d = int(bool(num & d))
        if _d == 1:
            if _b == 0 and _c == 1:
                print(-1)
                return
            elif (_b == 1 and _c == 0) or (_b == 0 and _c == 0):
                ans |= (num)
        else:
            if _b == 1 and _c == 0:
                print(-1)
                return
            elif (_b == 1 and _c == 1):
                ans |= (num)
    
    print(ans)

 
 
 
 
T = I()
for _ in range(T):
    solve()