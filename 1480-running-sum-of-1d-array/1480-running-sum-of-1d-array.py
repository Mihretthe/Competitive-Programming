class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix=[nums[0]]
        for i in nums[1:]:
            prefix.append(prefix[-1]+i)
        return prefix