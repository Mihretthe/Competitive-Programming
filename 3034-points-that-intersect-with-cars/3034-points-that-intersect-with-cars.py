class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:

        length = 0

        for i, j in nums:
            length = max(length, i, j)

        prefix = [0] * (length + 1)

        for start, end in nums:
            prefix[start] += 1
            if end + 1 < length:
                prefix[end + 1] -= 1
        
        for i in range(1, length + 1):
            prefix[i] += prefix[i - 1]
        
        prefix = prefix[1:]

        zeros = prefix.count(0)

        return length - zeros