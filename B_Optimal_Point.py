from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter

def solve():
    n, k = II()
    counter = Counter()



    for _ in range(n):
        start, end = II() 
        if k >= start and k <= end:
            for i in range(start, end + 1):    
                counter[(i, k)] += 1
    
    if not counter:
        print("NO")
    else:
        for key, value in counter.items():
            if key != (k, k):
                if value == counter[(k, k)]:
                    print("NO")
                    break
        else:
            print("YES")

        
    
    

    
        

 
    
 
 
T = I()
for _ in range(T):
    solve()