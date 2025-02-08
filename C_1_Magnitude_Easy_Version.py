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

    c = 0

    last = 0

    for i in range(n):
        if a[i] < 0:
            last = i


    for i in range(n):
        if i == last and a[last] < 0:
            c = abs(c + a[i])
            
        else:
            c += a[i]
       

    print(abs(c))


 
 
 
 
T = I()
for _ in range(T):
    solve()
 
 


