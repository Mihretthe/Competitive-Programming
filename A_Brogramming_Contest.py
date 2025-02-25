from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    s = S()
    
    if s[0] == "0":
        count = 0
    else:
        count = 1
            
    for i in range(1, n):
        if (s[i] == "0" and s[i - 1] == "1") or (s[i] == "1" and s[i - 1] == "0"):
            count += 1
        
    print(count)
        
        
 
 
 
T = I()
for _ in range(T):
    solve()