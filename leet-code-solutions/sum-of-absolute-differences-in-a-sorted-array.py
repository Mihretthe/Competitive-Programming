class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = []
        prefix = [nums[0]]
        for i in range(1, length):
            prefix.append(prefix[-1] + nums[i])
        
        max_sum = prefix[-1]
        for i in range(length):
            value = ((nums[i] * (i + 1)) - prefix[i]) + ((max_sum - prefix[i]) - (nums[i] * (length - i - 1)))
            result.append(value)
        
        return result
