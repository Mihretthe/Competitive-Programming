from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import deque

def solve():
    n, m = II()
    a = IL()

    deck = deque(enumerate(a))

    while len(deck) > 1:
        index, child = deck.popleft()
        child -= m

        if child > 0:
            deck.append((index, child))

    print(deck[0][0] + 1) 
 
 
 
 
T = 1
for _ in range(T):
    solve()