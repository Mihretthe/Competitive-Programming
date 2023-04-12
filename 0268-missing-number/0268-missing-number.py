class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        a=list((range(len(nums)+1)))
        for i in a:
            if i in nums:
                continue
            else:
                return i