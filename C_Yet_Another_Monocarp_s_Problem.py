from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, h = II()
    a = IL()

    def check(mid):
        answer = 0
        for i in range(n - 1):
            answer += (min(mid + a[i], a[i + 1]) - a[i])
        answer += mid
        return answer >= h


    left = 0
    right = h 

    while left + 1 < right:
        mid = (left + right) // 2

        if check(mid):
            right = mid
        else:
            left = mid
    
    print(right)
 
 
 
 
T = I()
for _ in range(T):
    solve()