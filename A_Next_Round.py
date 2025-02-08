from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, k = II()
    nums = IL()
    count = 0
    
    for i in nums:
        if i > 0 and i >= nums[k - 1]:
            count += 1
        else:
            break
    print(count)

 
 
 
 
T = 1
for _ in range(T):
    solve()