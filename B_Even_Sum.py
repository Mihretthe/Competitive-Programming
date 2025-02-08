from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import inf

def solve():
    n = I()
    a = IL()

    evens = []
    odds = []

    for num in a:
        if num % 2:
            odds.append(num)
        else:
            evens.append(num)
    
    

    if len(odds) % 2 == 0:
        print(0)
        return
    
    mini = inf
    for i in range(len(odds)):
        mini_odd = odds[i]
        odd = 0
        while mini_odd % 2:
            mini_odd //= 2
            odd += 1
        mini = min(mini, odd)

    for i in range(len(evens)):
        mini_even = evens[i]
        even = 0
        while mini_even % 2 == 0:
            mini_even //= 2
            even += 1
        mini = min(mini, even)
    
    print(mini)
    


    

 
 
 
 
T = I()
for _ in range(T):
    solve()