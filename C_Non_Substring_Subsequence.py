from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, q = II()
    s = S()
    
    for _ in range(q):
        l, r = II()
        
        middle = s[l - 1:r]
        if middle[0] in s[:l - 1] or middle[-1] in s[r:]:
            print("YES")
        else:
            print("NO")
        
    
 
 
 
 
T = I()
for _ in range(T):
    solve()