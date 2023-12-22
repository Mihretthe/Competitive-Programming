class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        zeros = [0] * n
        ones = [0] * n

        countz = 0
        counto = 0

        for i in range(n):
            zeros[i] = countz
            if s[i] == "0":
                countz += 1
            

        for i in range(n - 1, -1, -1):
            if s[i] == "1":
                counto += 1
            ones[i] = counto


        m = 0
        for i in range(1, n):
            m = max(m, zeros[i] + ones[i])

        return m


