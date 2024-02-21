class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        letters = "abcdefghijklmnopqrstuvwxyz"
        length = len(palindrome)
        palindrome = list(palindrome)
        
        if length == 1:
            return ""

        for i in range(length // 2):
            if letters.index(palindrome[i]) > 0:
                palindrome[i] = "a"
                return "".join(palindrome)
        else:
            if palindrome[-1] == "a":
                palindrome[-1] = "b"
            else:
                palindrome[-1] = "a"

        return "".join(palindrome)