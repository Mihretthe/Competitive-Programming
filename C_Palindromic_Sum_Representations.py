from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def isPal(num):
    return str(num) == str(num)[::-1]

dp = [0] * (40001)
dp[0] = 1
array = []
for i in range(1, 40001):
    if isPal(i):
        array.append(i)
        
for i in array:
    for j in range(i, 40001):        
        dp[j] += dp[j - i] 
        dp[j]  %= 1000000007

def solve():
    n = I()
    print(dp[n])
           

 
 
 
T = I()
for _ in range(T):
    solve()