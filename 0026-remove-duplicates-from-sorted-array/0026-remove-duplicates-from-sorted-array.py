class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        t=[]
        i=0
        while i<len(nums):
            a=nums[i]
            t.append(nums[i])
            i+=nums.count(nums[i])
        print(t)
        j=0
        while j<len(t):
            nums[j]=t[j]
            j+=1
        return len(t)
            