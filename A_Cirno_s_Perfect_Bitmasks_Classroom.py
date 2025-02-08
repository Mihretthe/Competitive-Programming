from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def isOn(x, k):
    number = 1 << k
    return number & x


def solve():
    x = I()
    not_x = ~x
    if x == 1:
        print(3)
        return

    not_x += 1
    not_x &= x

    if x == not_x:
        print(not_x + 1)
    else:
        print(not_x)
    
    

 
 
T = I()
for _ in range(T):
    solve()