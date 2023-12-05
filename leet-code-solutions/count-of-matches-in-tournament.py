class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n > 1:
            count += n // 2
            if n % 2 == 0:
                n //= 2
            else:
                n = int((n - 1) / 2) + 1
            
        return count