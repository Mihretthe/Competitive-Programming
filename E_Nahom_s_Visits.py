from collections import *
# for _ in range(int(input())):
#     n,m,d = map(int, input().split())
#     arr = list(map(int, input().split()))
#     memo = defaultdict(int)
#     def dp(ind, last,cnt):
#         global m, d
#         if cnt==m or ind==len(arr):
#             return 0
#         if (ind,last,cnt) not in memo:
#             take = arr[ind] - d*(ind-last) + dp(ind+1, ind, cnt+1)
#             leave = dp(ind+1, last, cnt)
#             memo[(ind, last, cnt)] = max(take, leave)
#         return memo[(ind, last, cnt)]
    
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    for _ in range(int(input())):
        n,m,d = map(int, input().split())
        arr = list(map(int, input().split()))
        memo = defaultdict(int)
        def dp(ind, last,cnt):
            # global m, d
            if cnt==m or ind==len(arr):
                return 0
            if (ind,last,cnt) not in memo:
                take = arr[ind] - d*(ind-last) + dp(ind+1, ind, cnt+1)
                leave = dp(ind+1, last, cnt)
                memo[(ind, last, cnt)] = max(take, leave)
            return memo[(ind, last, cnt)]
        print(dp(0,-1,0))
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
    
    