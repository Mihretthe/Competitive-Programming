from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict 
def solve():
    n, q = II()
    a = S()
    b = S()
    counter_a = [[0 for _ in range(n + 1)] for _ in range(26)]
    counter_b = [[0 for _ in range(n + 1)] for _ in range(26)]

    for k in range(n):
        i = a[k]
        counter_a[ord(i)-97][k] += 1
    
    for k in range(n):
        i = b[k]
        counter_b[ord(i)-97][k] += 1
    
    for i in range(26):
        for j in range(1, n):
            counter_a[i][j] += counter_a[i][j - 1]
        
        for j in range(1, n):
            counter_b[i][j] += counter_b[i][j - 1]
        
    

    for _ in range(q):
        l, r = II()
        count_a = 0
        for i in range(26):
            count_a += (counter_a[i][r-1] - counter_a[i][l-1 - 1])
        count_b = 0
        for i in range(26):
            count_b += (counter_b[i][r-1] - counter_b[i][l-1 - 1])
        print(abs(count_a - count_b))

        
    print(counter_a)
    print(counter_b)

 
 
 
T = I()
for _ in range(T):
    solve()
    print()