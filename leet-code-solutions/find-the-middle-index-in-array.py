class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [0]
        length = len(nums)

        for index in range(length):
            prefix.append(prefix[-1] + nums[index])

        for index in range(length):
            if prefix[index] == (prefix[-1]  - prefix[index + 1]):
                return index
        return -1