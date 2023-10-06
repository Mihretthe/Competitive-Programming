class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
               
        def dp(num):
            if num <= 3:
                return num
            
            ans = num
            for i in range(2,num):
                m = i * dp(num - i)
                if ans < m:
                    ans = m
            return ans 
        if n <= 3:
            return n - 1
        
        return dp(n) 