class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        v=s[::-1]
        if s==v:
            return True
        else:
            return False