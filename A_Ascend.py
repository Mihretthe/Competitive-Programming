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
    if n == 1:
        print(1)
        return

    left = 0
    right = 1
    
    maxi = 0
    num = a[0]

    while right < n:
        if num < a[right]:
            num = a[right]
            right += 1
        else:
            left = right
            num = a[left]
            right += 1
        maxi = max(maxi, right - left)
    
    print(maxi)


 
 
 
 
T = 1
for _ in range(T):
    solve()