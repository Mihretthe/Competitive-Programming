class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        ans = 0
        odd = 0
        

        for key, value in counter.items():
            
            if value % 2 == 0:
                ans += value
            else:
                odd += 1
                ans += value - 1

        if odd:
            ans += 1
        return ans