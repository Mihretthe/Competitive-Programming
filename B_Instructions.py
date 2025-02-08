
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        memo = {}
        def dp(index):
            
            if index >= n:
                return 0
            if index not in memo:
                memo[index] = a[index] + dp(index + a[index])
            return memo[index]
        maxi = 0
        for i in range(n):
            maxi = max(maxi, (dp(i)))
        print(maxi)
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
