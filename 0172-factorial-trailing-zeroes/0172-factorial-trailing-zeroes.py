class Solution:
    def trailingZeroes(self, n: int) -> int:
        prod = 1

        for i in range(1, n + 1):
            prod *= i
        
        count = 0

        while prod % 10 == 0:
            count += 1
            prod //= 10
        
        return count