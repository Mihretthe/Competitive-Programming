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

    end = n - 1
    count = 0

    while end >= 0 and s[end] == ")":
        end -= 1
        count += 1
    
    if count > n - count:
        print("Yes")
    else:
        print("No")

 
 
 
 
T = I()
for _ in range(T):
    solve()