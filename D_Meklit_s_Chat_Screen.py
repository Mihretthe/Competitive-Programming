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
    a = IL()
    
    deck = deque()
    my_set = set()
    
    for i in range(n):
        if a[i] not in my_set:
            if len(deck) == k:                
                my_set.remove(deck.pop())
            deck.appendleft(a[i])
            my_set.add(a[i])
    
    print(len(deck))
    print(*deck)
            
    
    
 
 
 
 
T = 1
for _ in range(T):
    solve()