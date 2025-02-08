from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n, m = II()
    a = IL()

    
    subarrays = []
    prefix = [0]

    for i in range(n):
        prefix.append(prefix[-1] + a[i])

    for _ in range(m):
        a, b = II()
        subarrays.append((a, b))

    
    def calc(interval):
        l, r = interval
        l -= 1
        return prefix[r] - prefix[l]

    memo = {}
    def dp(index):
        if index == m:
            return 0
        
        if index in memo:
            return memo[index]
        
        take = calc(subarrays[index]) + dp(index + 1)
        leave = dp(index + 1)

        memo[index] = max(take, leave)

        return memo[index]

    print(dp(0))

        
        
 
 
 
 
T = 1
for _ in range(T):
    solve()