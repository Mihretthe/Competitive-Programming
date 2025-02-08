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
    for i in range(n):
        a[i] = (a[i], i)
    a.sort()
    left = 0
    right = n - 1

    while left < right:
        print(a[left][1] + 1, a[right][1] + 1)
        left += 1
        right -= 1
    

 
 
T = 1
for _ in range(T):
    solve()