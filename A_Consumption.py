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
    b = IL()
    
    tot = sum(a)
    b.sort(reverse=True)
    
    b = b[:2]
    
    if sum(b) >= tot:
        print("YES")
    else:
        print("NO")
 
 
 
 
T = 1
for _ in range(T):
    solve()