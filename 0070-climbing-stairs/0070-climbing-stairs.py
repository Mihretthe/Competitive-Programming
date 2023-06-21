class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def help(n):
            if n == 1 or n == 0:
                return 1
            if n in memo:
                return memo[n]  
            memo[n] = help(n - 1) + help(n - 2)
            return memo[n]
        
        return help(n)