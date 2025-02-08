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
    
    s = sorted(s)
    ans = []
    l = 0
    r = n - 1

    while l <= r:
        ans.append(s[l])
        if l == r:
            break
        ans.append(s[r])
        l += 1
        r -= 1
    print("".join(ans))
    
        
    
 
 
 
T = I()
for _ in range(T):
    solve()