from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def solve():
    n = I()
    a = IL()
    
    maxi = max(a)

    index = []

    for i in range(n):
        if a[i] == maxi:
            index.append(i)
    
    both = False
    even = False
    odd = False

    for i in index:
        if i % 2:
            odd = True
        else:
            even = True

    both = odd and even

    if even:
        ans = maxi + ceil(n / 2)
    elif odd:
        ans = maxi + n // 2

    print(ans)
    


 
 
 
 
T = I()
for _ in range(T):
    solve()