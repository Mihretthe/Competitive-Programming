from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, m, till = II()
    s = S()
    memo = {}
    def dp(index, till):
        if till < 0:
            return False

        if index >= n:
            return True
        
        if (index, till) in memo:
            return memo[(index, till)]
        
        
        if s[index] == 'L':
            truth = False
            for i in range(1, m + 1):
                truth = truth or dp(index + i, till)
            memo[(index, till)] = truth
        elif s[index] == "W":
            memo[(index, till)] = dp(index + 1, till - 1)
        else:
            memo[(index, till)] = False
        return memo[(index, till)]      
    
      
    if (dp(0, till) or dp(m - 1, till)):
        print("YES")
    else:
        print("NO")


        






 
 
 
 
T = I()
for _ in range(T):
    solve()