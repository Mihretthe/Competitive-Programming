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

    ans = []

    left = 0
    i = 1

    while left < n:
        ans.append(s[left])
        left += i 
        i += 1
    
    print("".join(ans))

 
 
 
T = 1
for _ in range(T):
    solve()