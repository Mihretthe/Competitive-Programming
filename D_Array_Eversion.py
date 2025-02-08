from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    a = IL()
    maxi = max(a)
    mx = a[-1]
    count = 0

    for i in range(n - 1, -1, -1):
        if mx == maxi:
            break
        if a[i] > mx:
            mx = a[i]
            count += 1
        

    print(count)


    
 
 
 
 
T = I()
for _ in range(T):
    solve()