def I(): return int(input())
 
def II(): return map(int, input().split())
 
def IL(): return list(map(int, input().split()))
 
def SIL(): return sorted(map(int, input().split()),)

def S() : return input()

def SL() : return list(input().split())

from math import prod


def solve():

    length = I()
    nums = IL()

    path = []
    answer = float('-inf')

    nums.sort()
    if length > 10:
        nums = nums[:5] + nums[-5:]
        length = 10


    def backtrack(index):
        nonlocal answer, length
        if len(path[:]) == 5:
            answer = max(answer, prod(path[:]))
            return 
        
        for i in range(index, length):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()



    backtrack(0)
    print(answer)
    
   
T = I()
for _ in range(T):
    solve()