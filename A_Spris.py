from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    a = I()
    b = I()
    c = I()
    num = 0
    
    while a:
        
        if a * 2 > b or a * 4 > c:
            a -= 1
        else:
            num = a + a * 2 + a * 4
            break

    print(num)
    
 
 
T = 1
for _ in range(T):
    solve()