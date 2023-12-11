class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1

        
        ans = 0
        if not nums:
            return 0

        for i in range(1,len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            if nums[i - 1] + 1 == nums[i]:
                count += 1

            else:
                ans = max(ans, count)
                count = 1
        ans = max(ans, count)

        return ans



             