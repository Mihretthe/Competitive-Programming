class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]
        suffix = [0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        for i in nums[::-1]:
            suffix.append(suffix[-1]+i)
        suffix = suffix[:-1][::-1]
        n = len(suffix)
        for i in range(n):
            if prefix[i] == suffix[i]:
                return i
        return -1