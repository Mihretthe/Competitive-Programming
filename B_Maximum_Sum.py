from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())



def solve():
    length, k = II()
    nums = IL()
    total = 0

    max_sum = float("-inf")
    max_end = 0

    for i in range(length):
        total += nums[i]

        max_end += nums[i]
        max_sum =  max(max_sum, max_end)
        max_end = max(max_end, 0)

    max_sum = max(0, max_sum)

    
    
    print((total + (2**k - 1) * max_sum) % 1000000007)
    # print(max_sum)
        
        
    
    
    
 
 
 
 
T = I()
for _ in range(T):
    solve()