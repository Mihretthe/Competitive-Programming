from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import deque

def solve():
    n, k = II()
    array = []

    deck = deque(range(1, n + 1))
    
    for i in range(1, n + 1):
        if i % k == 0:
            array.append(deck.popleft())
        else:
            array.append(deck.pop())
    
    print(*array)
 
 
 
T = I()
for _ in range(T):
    solve()