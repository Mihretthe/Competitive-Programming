class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        a=[]
        while i<len(nums):
            if nums.count(nums[i])==2:
                i+=2
            else:
                a.append(nums[i])
                i+=1
        return a