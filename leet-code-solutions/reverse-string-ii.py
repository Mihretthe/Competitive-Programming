class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = 0
        r = k

        ans = ""

        if len(s) < k:
            return s[::-1]

        while l <= len(s) and r <= len(s):
            ans += s[l:r][::-1]
            l = r
            r = l + k
            ans += s[l:r]
            l = r
            r = l + k

        return ans + s[l:][::-1]