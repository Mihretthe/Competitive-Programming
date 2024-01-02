class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1
        letters = "abcdefghijklmnopqrstuvwxyz0123456789"

        while l <= r:
            if s[l] not in letters:
                l += 1
            elif s[r] not in letters:
                r -= 1
            elif s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] != s[r]:
                return False

        return True