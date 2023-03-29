class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t=[]
        i=0
        while i<len(nums):
            t.append(nums[i])
            i+=nums.count(nums[i])
        j=0
        while j<len(t):
            nums[j]=t[j]
            j+=1
        return len(t)
            