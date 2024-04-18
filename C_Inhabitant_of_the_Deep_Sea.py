from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def solve():
    n, k = II()
    a = IL()
    count = 0
    
    left = 0
    right = n - 1

    while left <= right and k > 0:
        mini = min(a[left], a[right])
        if k > 2 * mini:
            k -= 2 * mini
            a[left] -= mini
            a[right] -= mini
        
            if a[left] <= 0:
                left += 1
            
            if a[right] <= 0:
                right -= 1
        else:
            print(count + 1)
            return
        
        count += 1

    print(count)

    


 
 
 
 
T = I()
for _ in range(T):
    solve()