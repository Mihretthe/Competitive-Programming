from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())



def solve():
    s = S()
    t = S()
    
    n = len(s)
    m = len(t)
    
    mini = n + m
    
    for index in range(m):
        j = index
        i = 0
        
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        diff = j - index
        mini = min(mini, m + n - diff)
    print(mini)
            
        
        
 
 
T = I()
for _ in range(T):
    solve()