from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import Counter

def solve():
    n, m = II()
    nums = IL()
    
    counter = Counter()
    answer = []
    left = 0
    
    for right in range(n):
        counter[nums[right]] += 1
        
        while len(counter) > m:
            counter[nums[left]] -= 1
            if counter[nums[left]] == 0:
                del counter[nums[left]]
            left += 1
        if answer:
            if answer[-1] - answer[0] < right - left:
                answer = [left + 1, right + 1]
        else:
            answer = [left + 1, right + 1]
    
    print(*answer)
 
 
 
 
T = 1
for _ in range(T):
    solve()