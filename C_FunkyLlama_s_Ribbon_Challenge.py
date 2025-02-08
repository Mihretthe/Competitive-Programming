
import sys, threading

input = lambda: sys.stdin.readline().strip()


def main():
    n, a, b, c = map(int, input().split())
    memo = {}
    
    def dp(amount):
        if amount == 0:            
            return 0
        if amount in memo:
            return memo[amount]
        
        answer = float('-inf')
        for i in [a,b,c]:
            if amount >= i:                
                answer = max(answer, 1 + dp(amount - i))

        memo[amount] = answer

        return memo[amount]

    
    print(max(0, (dp(n)))) 



        
        
        
        
    
    
            
        


    
    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
