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
                break
        else:
            palindrome[-1] = "b"
            

        return "".join(palindrome)