
import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    a = list(map(int, input().split()))

    memo = {}
    def dp(index):
        if index == 0:
            return 0
        if index == 1:
            return abs(a[index] - a[index - 1])
        if index not in memo:
            memo[index] = min(abs(a[index] - a[index - 1]) + dp(index - 1), abs(a[index] - a[index - 2]) + dp(index - 2))
        return memo[index]
    print(dp(n - 1))

if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
