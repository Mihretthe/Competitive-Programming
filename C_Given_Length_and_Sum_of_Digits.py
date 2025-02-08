from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    m, s = II()

    if s > 9 * m:
        print(-1, -1)
        return
    
    if s == 0:
        if m == 1:
            print(0, 0)
        else:
            print(-1, -1)
        return
    
    mini = ["0"] * m
    maxi = ["0"] * m
    s2 = s 
    mini[0] = "1"
    s2 -= 1

    for i in range(m - 1, -1, -1):
        num = min(s2, 9)
        s2 -= num
        mini[i] = str(int(mini[i]) + num)
        if s2 == 0:
            break

    for i in range(m):
        num = min(s, 9)
        s -= num
        maxi[i] = str(num)
        if s == 0:
            break

    print("".join(mini), "".join(maxi))





 
 
 
 
T = 1
for _ in range(T):
    solve()