from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from math import ceil

def createArray(num):
    n = num
    array = []

    while n < 1000000001:
        array.append(n)
        n *= num
    
    return array

def solve():
    k, l1, r1, l2, r2 = II()
    
    array = (createArray(k))
    count = 0
    for num in array:
        left = max(l1, ceil(l2 / num))
        right = min(r1, r2 // num)
        
        count += max(0, right - left + 1)
       
    n = max(0, min(r1, r2) - max(l1, l2) + 1)
    print(count + n)


         
        

 
T = I()
for _ in range(T):
    solve()