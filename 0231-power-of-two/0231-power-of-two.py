class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n==0:
            return False
        return n%2==0 and self.isPowerOfTwo(n//2)