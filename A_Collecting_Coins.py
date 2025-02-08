from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    coins = IL()
    n = coins[-1]

    coins.pop()
    
    coins.sort()

    till = 0
    for i in range(2):
        till += (coins[-1] - coins[i])
    
    n -= till

    if n % 3 or n < 0:
        print("NO")
    else:
        print("YES")


 
 
 
 
T =I()
for _ in range(T):
    solve()