class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)//3
        a=[]
        nums.sort()
        i=0
        while i<len(nums):
            if nums.count(nums[i])>n:
                a.append(nums[i])
            i+=nums.count(nums[i])
        return a
        