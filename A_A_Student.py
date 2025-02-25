from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def calc(a, b, c):
    if a > b and a > c:
        return 0

    return max(b, c) - a + 1

def solve():
    a, b, c = II()
    print(calc(a, b, c), end = " ")
    print(calc(b, a, c), end = " ")
    print(calc(c, a, b))
    
    
    
        
 
 
 
 
T = I()
for _ in range(T):
    solve()