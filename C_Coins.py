from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    memo = {}
    def dp(n):
        if n in memo:
            return memo[n]
        if n < 3:
            return n
        if n < 5:
            return n - 3
        
        five = dp(n - 5)
        three = dp(n - 3)

        memo[n] = min(five, three)
        return memo[n]

    print(dp(n))
        
 
 
 
T = I()
for _ in range(T):
    solve()