from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict

from math import prod


def calculate(hashmap):
    total = sum(hashmap.values())
    answer = 0
    

    for key, value in hashmap.items():
        total -= value
        if total == 0:
            break
        answer += (value * total)
    
    return answer



def solve():
    n = I()
    nums = IL()
    

    pairs = [0]
    
    def helper(a, b, c):

        first = defaultdict(dict)

        for i in range(n - 2):
            tup = (nums[i + a], nums[i + b])
            if nums[i + c] in first[tup]:
                first[tup][nums[i + c]] += 1
            else:
                first[tup][nums[i + c]] = 1
        
        for key, value in first.items():
            pairs[0] += calculate(value)
    


    helper(0, 1, 2)
    helper(0, 2, 1)
    helper(1, 2, 0)

        
    print(pairs[0]) 
    
 
 
T = I()
for _ in range(T):
    solve()