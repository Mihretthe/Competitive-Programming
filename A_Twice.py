from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter

def solve():
    n = I()
    a = IL()
    counter = Counter(a)

    score = 0

    for key, value in counter.items():
        score += (value // 2)
    
    print(score)
 
 
 
 
T = I()
for _ in range(T):
    solve()