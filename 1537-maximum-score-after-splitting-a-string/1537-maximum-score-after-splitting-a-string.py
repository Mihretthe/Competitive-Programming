class Solution:
    def maxScore(self, s: str) -> int:
        length = len(s)
        zeros = [0] * (length)
        ones = [0] * (length)

        for i in range(length):
            if s[i] == "1":
                ones[i] += 1
            else:
                zeros[i] += 1
        ones = ones[::-1]
        for i in range(1,length):
            ones[i] += ones[i - 1]
            zeros[i] += zeros[i - 1]
        ones = ones[:-1]
        zeros = zeros[:-1]
        ones = ones[::-1]
        max_sum = 0
        for i, j in zip(zeros, ones):
            if i + j > max_sum:
                max_sum = i + j

        return max_sum
    