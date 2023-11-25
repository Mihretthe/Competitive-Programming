class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1] + i)          
        for i in range(len(nums)):
            ans.append((nums[i] * i) - prefix[i] + prefix[len(nums)] - prefix[i + 1] - (nums[i] * (len(nums) - i - 1)))
            
        return ans
    