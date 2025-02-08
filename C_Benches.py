from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


from math import lcm

def solve():
    n = I()
    m = I()
    a = []
    mini = float('inf')
    maxi = 0
    for _ in range(n):
        num = I()
        a.append(num)
        maxi = max(maxi, num)
    tot = 0
    for num in a:
        tot += (maxi - num)
    
    if m < tot:
        print(maxi, maxi + m)
    else:
        remain = m - tot
        print(maxi + (remain // n + bool(remain % n)), maxi + m)
        


    



    
    
 
 
 
 
T = 1
for _ in range(T):
    solve()