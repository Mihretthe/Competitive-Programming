from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import deque

def solve():
    n, s = II()
    a = IL()
    b = IL()
    s -= 1
    if a[0] == 0:
        print("NO")
        return
    if a[0] == 1 and a[s] == 1:
        print("YES")
        return
    
    if a[0] == 1 and b[s] == 1:
        for i in range(s, n):
            if a[i] == b[i] == 1:
                print("YES")
                return

    print("NO")        


 
 
 
 
T = 1
for _ in range(T):
    solve()