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

    array = []

    for key, val in counter.items():
        if val == 1:
            array.append(key)
    
    if not array:
        print(-1)
        return 

    mini = min(array)
    print(a.index(mini) + 1)
 
 
 
 
T = I()
for _ in range(T):
    solve()