from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import sqrt

def solve():
    n = I()
    s = S()
    ones = s.count("1")
    zeros = s.count("0")

    sq = sqrt(n)
    if sq != int(sq):
        print("No")
        return
    
    if zeros == (sq - 2) ** 2:
        print("Yes")
    else:
        print("No")


 
 
 
T = I()
for _ in range(T):
    solve()