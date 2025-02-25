from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, k = II()
    my_string = []
    
    def helper(string):
        print(string)

    
    for _ in range(n):
        my_string.append(S())
    
    def dp(index):
        
        if index == n:
            return []
        
        take  = [my_string[index]] + dp(index + 1)
        leave = dp(index + 1)
        
        return helper(take) + helper(leave)

    dp(0)
    
        
        
    
    
 
 
 
T = I()
for _ in range(T):
    solve()