from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from bisect import bisect_left

def solve():
    s = S()
    n = len(s)

    poss = []
    another = [0]

    for i in range(len(s)):
        if s[i] == "a":
            poss.append(i)
        if s[i] == "b":
            another.append(another[-1] + 1)
        else:
            another.append(another[-1])

    count = len(poss)

    for i in (poss):
        count += another[-1] - another[i]

    print(count)



    
    



 
 
 
 
T = 1
for _ in range(T):
    solve()