from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

from collections import defaultdict, Counter

def solve():
    # Start from the mini the dp is going to end at the maxi
    # else it is going to end at the mini

    n = I()
    a = IL()

    counter = Counter(a)
    maxi = max(a)
    memo = {}

    def dp(value):
        if value in memo:
            return memo[value]
        
        if value > maxi:
            return 0
        
        if value not in counter:
            return dp(value + 1)
        
        memo[value] = max(counter[value] * value + dp(value + 2), dp(value + 1))
        return memo[value]

    print(dp(min(a)))



 
 
 

import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    solve()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
