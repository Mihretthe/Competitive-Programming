from sys import stdin

def I(): return int(stdin.readline().strip())
 
def II(): return map(int, stdin.readline().strip().split())
 
def IL(): return list(map(int, stdin.readline().strip().split()))
 
def SIL(): return sorted(map(int, stdin.readline().strip().split()),)

def S() : return stdin.readline().strip()

def SL() : return list(stdin.readline().strip().split())

def solve():
    n, m, k = II()

    def inbound(row, col):
        return 0 <= row < n and 0 <= col < m

    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if  i == 0 and j == 0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + j + 1
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + i + 1
            else:
                dp[i][j] = dp[i][j - 1] + i + 1 
        # print(dp[i])

    if (dp[-1][-1]) == k:
        print("YES")
    else:
        print("NO")

    

    
 
 
 



import sys, threading

input = lambda: sys.stdin.readline().strip()

def main():
    T = I()
    for _ in range(T):
        solve()
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
