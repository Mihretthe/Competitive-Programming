from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import deque


def solve():
    s = deque(S())
    t = deque(S())
    count = 0
    copy = False
    while s and t and s[0] == t[0]:
        s.popleft()
        t.popleft()
        count += 1
        copy = True

    if copy:
        count += 1
    
    print(count + len(s) + len(t))


 
 
 
 
T = I()
for _ in range(T):
    solve()