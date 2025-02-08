from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()

    maxi = 0
    mul = 1
    for i in range(n, 0, -1):
        maxi += (mul * i)
        mul += 1
    
    print(maxi)
    


   

 
 
 
 
T = I()
for _ in range(T):
    solve()