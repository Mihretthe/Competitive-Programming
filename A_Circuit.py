from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    a = IL()

    ones = 0
    zeros = 0

    for i in a:
        if i == 0:
            zeros += 1
        else:
            ones += 1
    
    mini = 0

    if ones % 2:
        mini = 1
        
    maxi = 0
    if ones > n:
        maxi = ones - ((ones - n) * 2)
    else:
        maxi = ones

    print(mini, maxi)
 
 
 
 
T = I()
for _ in range(T):
    solve()