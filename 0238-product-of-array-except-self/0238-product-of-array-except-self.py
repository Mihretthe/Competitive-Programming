class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        ans = []
        n = len(nums)
        for i in nums:
            ans.append(prefix)
            prefix*=i
        suffix = 1
        for i in range(n-1,-1,-1):
            ans[i]*= suffix
            suffix*= nums[i]
        return ans