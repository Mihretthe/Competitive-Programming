from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())


def solve():
    n = I()
    nums = IL()
    nums = [i % 2 for i in nums]
    
    evens = 0
    odds = 0
    
    for num in nums:
        if num % 2:
            odds += 1
        else:
            evens += 1
    
    if odds > evens:
        # should start with odd number
        pass
    elif odds < evens:
        # should start with even number
        pass
    else:
        # can start by both, but would be great if it starts with the number at zeros 
        # because we are asked the minimum number of swaps
        
        left = 0
        right = 1
        
        while right < n:
            pass
            
        
 
 
 
 
T = I()
for _ in range(T):
    solve()