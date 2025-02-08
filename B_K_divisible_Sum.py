from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


from math import lcm

def solve():
    n, k = II()
    if k >= n:
        print(k // n + bool(k % n))
    else:
        add = (k - (n % k)) if n % k else 0
        left = n + add
        right = lcm(n, k) 
        while left <= right:
            mid = (left + right) // 2
            if mid == n:
                left = mid 
                break
            elif mid < n:
                left = mid + k
            else:
                right = mid - k
        
        


        print(left // n + bool(left % n))
 
 
 
 
T = I()
for _ in range(T):
    solve()