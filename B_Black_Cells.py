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

    def check(mid):
        
        index = 1
        count = 0

        while index < n:
            if count == 2:
                return False
            if a[index] - a[index - 1] > mid:
                count += 1
                index += 1
            else:
                index += 2
        
        count += index == n
        if count >= 2:
            return False
        return True







    left = 0
    right = 10**18

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