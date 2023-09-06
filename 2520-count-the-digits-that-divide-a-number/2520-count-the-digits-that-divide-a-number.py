class Solution:
    def countDigits(self, num: int) -> int:
        s = str(num)
        ans = 0
        for i in s:
            if num % int(i) == 0:
                ans += 1
        return ans 