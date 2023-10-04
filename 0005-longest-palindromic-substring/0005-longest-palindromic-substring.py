class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = []
        i = 0
        while i < n - 1:
            j = n 
            while j > 0:
                if s[i:j] == s[i:j][::-1]:
                    ans.append(s[i:j])
                    break
                j -= 1
            i += 1
        ans.sort(key = lambda x: len(x))
        if ans:
            return ans[-1]
        return s[0]