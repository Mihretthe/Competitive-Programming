class Solution:
    def largestGoodInteger(self, num: str) -> str:
        m = ""
        l = 0
        r = 3
        n = len(num)

        while r <= n:
            if len(set(num[l:r])) == 1:
                if m and int(m) < int(num[l:r]):
                    m = num[l:r]
                elif m == "":
                    m = num[l:r]

            l += 1
            r += 1
        return m
