from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    s = S()
    n = len(s)
    count = 1

    cou = 0

    for i in range(1, n):
        if s[i - 1] == "1" and s[i] == "0":
            count += 1
        elif s[i - 1] == "0" and s[i] == "1":
            cou += 1
    

    
    print(count + max(0, cou - 1))
 
 
 
 
T = I()
for _ in range(T):
    solve()